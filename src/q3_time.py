import cProfile
import pstats
import io
from q3_memory import q3_memory

def profile(func):
    """
    Decorador para medir el tiempo de ejecución de una función usando cProfile.

    Args:
        func: La función a perfilar.

    Returns:
        Una función envuelta que devuelve el resultado y el tiempo de ejecución.
    """
    def wrapper(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()  # Habilitar el profiler
        result = func(*args, **kwargs)
        pr.disable()  # Deshabilitar el profiler

        # Crear un objeto StringIO para capturar la salida
        s = io.StringIO()
        ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
        ps.print_stats()
        
        exec_time = sum(t[3] for t in ps.stats.values())  # Calcular tiempo total de ejecución
        return result, exec_time
    return wrapper
