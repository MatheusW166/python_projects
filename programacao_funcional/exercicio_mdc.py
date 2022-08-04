def mdc(*args):
    u, v = max(args), min(args)
    while u != v:
        if u > v:
            u -= v
        else:
            v -= u
    return u


def mdcRecursivo(*args):
    u, v = max(args), min(args)
    if u > v:
        return mdcRecursivo(u-v, v)
    return u if u == v else mdcRecursivo(u, v-u)


if __name__ == '__main__':
    print(mdcRecursivo(21, 7))
    print(mdcRecursivo(125, 40))
    print(mdcRecursivo(9, 564, 66, 3))
    print(mdcRecursivo(55, 22))
    print(mdcRecursivo(15, 150))
    print(mdcRecursivo(7, 9))
