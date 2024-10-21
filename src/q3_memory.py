from typing import List, Tuple
import json
from collections import Counter
import re

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    """
    Procesa un archivo JSON y devuelve los 10 usuarios más mencionados en los tweets.

    Args:
        file_path: Ruta al archivo JSON que contiene los tweets.

    Returns:
        Una lista de tuplas con el nombre del usuario mencionado y su frecuencia.
    """
    mention_counter = Counter()  # Contador para menciones

    try:
        with open(file_path, 'r') as file:
            for line in file:
                try:
                    tweet = json.loads(line)  # Carga el tweet desde JSON
                    mentions = re.findall(r'@(\w+)', tweet['content'])  # Extrae menciones
                    mention_counter.update(mentions)  # Actualiza el contador de menciones
                except (json.JSONDecodeError, KeyError) as e:
                    print(f"Error al procesar la línea: {line.strip()}\n{e}")
                    continue  # Ignorar errores y seguir procesando

    except FileNotFoundError:
        print(f"El archivo {file_path} no se encontró.")
        return []
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return []

    return mention_counter.most_common(10)  # Devuelve los 10 usuarios más mencionados
