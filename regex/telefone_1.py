import re


DDD = r'^(\(0?\d{2}\)|0?\d{2})\s?'
TEL = r'(\d{4,5})[\s-]?(\d{4})$'


def padronizar_telefone(telefone):
    pattern = DDD + TEL

    if not re.search(pattern, telefone):
        return None

    telefone_raw = re.sub(r'\D', '', telefone)
    formato = r'(\1) \2-\3'
    return re.sub(pattern, formato, telefone_raw)


def main():
    with open('./telefones.txt', 'r') as telefones:
        tels_padronizados = [padronizar_telefone(tel) for tel in telefones]
    for n in tels_padronizados:
        print(n)


if __name__ == '__main__':
    main()
