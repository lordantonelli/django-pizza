pedidos = [
    {
        'nome':'Mario',
        'sabor':'Portuguesa'
    },
    {
        'nome':'Marcos',
        'sabor':'Peperoni'
    }
]

for pedido in pedidos:
    print('Nome: {0}\nSabor: {1}\n'.format(pedido['nome'], pedido['sabor']))

