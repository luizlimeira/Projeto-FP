print("Olá tudo bem? antes de realizar o pedido, Qual nome você deseja na comanda?")
x = input("Digite nome: ")

print("PRONTO!!! Agora vamos ao pedido... ")

precos = {
    'id1': 60.0,
    'id2': 70.0,
    'id3': 89.9,
    'id4': 45.0,
    'id5': 15.0,
}

cardapio = [
    "1.Filé à parmegiana--> 60,0",
    "2.Peixe crocante --> 70,0",
    "3.Carne de sol do Maranhão --> 89,9",
    "4.Filé com fritas ---> 45,0",
    "5.Caldinho de feijão ---> 15,0",
]

for item in cardapio:
    print(item)

pedidos_cliente = []
valor_total = 0.0

pedido = input("Qual item você deseja pedir? (ex: id1): ")
if pedido in precos:
    pedidos_cliente.append(pedido)
    valor_total += precos[pedido]

print(f"Pedido feito por {x}: {pedidos_cliente}, Total: R$ {valor_total:.2f}")
