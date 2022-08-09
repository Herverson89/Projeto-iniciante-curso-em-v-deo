p = float(input('Qual é o preco do produto? R$:'))

d = p - (p * 5 / 100)

print("O produto que custava R$ {}, na promocao com desconto de 5% vai custar {}".format(p, d))
