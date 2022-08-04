def todos_params(*args, **kwargs):
    print('==========================')
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')
    print('==========================')


if __name__ == '__main__':
    todos_params('a', 'b', 'c')
    todos_params(1, 2, 3, legal=True, valor=12.99)
    todos_params('Ana', False, [1, 2, 3], tamanho='M', fragile=False)
    todos_params(primeiro='João', segundo='Maria')
    todos_params('Maria', primeiro='João')
    # Erro: todos_params(primeiro='João', 'Maria')
