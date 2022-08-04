from datetime import datetime
from loja import *


def main():
    cliente = Cliente('Matheus', 18)
    vendedor = Vendedor('Janiro Gomes', 21, 1250)

    compra1 = Compra(vendedor, 512, datetime.now())
    compra2 = Compra(vendedor, 1024, datetime(2021, 7, 6))

    cliente.registrar_compra(compra1)
    cliente.registrar_compra(compra2)

    print(f'Cliente: {cliente}', '(adulto)' if cliente.is_adult() else '')
    print(f'Vendedor: {vendedor}')

    valor_total = cliente.total_compras()
    qtd_compras = len(cliente.compras)

    print(f'Total: {valor_total} em {qtd_compras} compras')
    print(f'Última compra: {cliente.get_data_ultima_compra()}')

    print(bar())
    print(waz)

if __name__ == '__main__':
    main()
