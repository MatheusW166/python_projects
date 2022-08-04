from functools import wraps
from time import time


def execution_time(function):
    @wraps(function)  # Copiando metadados da function
    def wrapper(*args, **kwargs):
        inicio = time()
        function(*args, **kwargs)
        fim = time()
        print(f'[{function.__name__}]: {fim-inicio:.2f}s')
    return wrapper


@execution_time
def contador_infinito():
    for i in range(100000000):
        pass


@execution_time
def contador_parametrizado(limite):
    for i in range(limite):
        pass


contador_infinito()
contador_parametrizado(10000000)

print(contador_infinito.__name__)  # -> contador_infinito
print(contador_parametrizado.__name__)  # -> contador_parametrizado
