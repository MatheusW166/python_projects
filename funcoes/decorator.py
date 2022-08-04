def decorator(function):
    print(f'Decorando função: {function.__name__}')

    def wrapper(*args, **kwargs):
        print(f'Início da chamada da função: {function.__name__}')
        print(f'args: {args}')
        print(f'kwargs: {kwargs}')
        resultado = function(*args, **kwargs)
        print(f'Resultado da chamada: {resultado}')
        return resultado
    return wrapper


@decorator
# Substituindo a chamada pelo decorator
def soma(x, y):
    return x + y


@decorator
def sub(x, y):
    return x - y


if __name__ == '__main__':
    print(soma(2, y=2))
