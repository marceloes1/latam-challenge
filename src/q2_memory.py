from typing import List, Tuple
import json
from collections import Counter
import emoji

def q2_memory(filename: str) -> List[Tuple[str, int]]:
    """
    Procesa un archivo JSON y devuelve los 10 emojis más usados en los tweets.

    Args:
        filename: Ruta al archivo JSON que contiene los tweets.

    Returns:
        Una lista de tuplas con el emoji y su frecuencia.
    """
    emoji_counter = Counter()  # Contador para los emojis

    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    tweet = json.loads(line)  # Carga el tweet desde JSON
                    emojis = [char for char in tweet['content'] if emoji.is_emoji(char)]  # Extrae emojis
                    emoji_counter.update(emojis)  # Actualiza el contador de emojis
                except (json.JSONDecodeError, KeyError) as e:
                    print(f"Error al procesar la línea: {line.strip()}\n{e}")
                    continue  # Ignorar errores y seguir procesando

    except FileNotFoundError:
        print(f"El archivo {filename} no se encontró.")
        return []
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return []

    return emoji_counter.most_common(10)  # Devuelve los 10 emojis más comunes
