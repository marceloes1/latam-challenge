from typing import List, Tuple
from datetime import datetime
import json
from collections import defaultdict, Counter

def q1_memory(filename: str) -> List[Tuple[datetime.date, str]]:
    """
    Procesa un archivo JSON y devuelve las 10 fechas con más tweets,
    junto con el usuario más activo en esas fechas.

    Args:
        filename: Ruta al archivo JSON que contiene los tweets.

    Returns:
        Una lista de tuplas con la fecha y el nombre del usuario más activo.
    """
    date_counter = Counter()  # Contador para las fechas
    user_counter = defaultdict(Counter)  # Contador para usuarios por fecha

    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    tweet = json.loads(line)  # Carga el tweet desde JSON
                    date = tweet['date'][:10]  # Extrae la fecha
                    username = tweet['user']['username']  # Extrae el nombre del usuario
                    date_counter[date] += 1  # Incrementa el contador de fechas
                    user_counter[date][username] += 1  # Incrementa el contador del usuario
                except (json.JSONDecodeError, KeyError) as e:
                    print(f"Error al procesar la línea: {line.strip()}\n{e}")
                    continue  # Ignorar errores y seguir procesando

        top_dates = date_counter.most_common(10)  # Obtiene las 10 fechas más comunes
        result = [
            (datetime.strptime(date, '%Y-%m-%d').date(), user_counter[date].most_common(1)[0][0])
            for date, _ in top_dates
        ]

    except FileNotFoundError:
        print(f"El archivo {filename} no se encontró.")
        return []
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return []

    return result

