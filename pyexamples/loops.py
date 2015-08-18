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
    s = 'Nome: {0}\nSabor: {1}\n'
    print(s.format(pedido['nome'], pedido['sabor']))

