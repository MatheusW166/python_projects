def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n-1)


print(f'10! = {fatorial(10)}')
