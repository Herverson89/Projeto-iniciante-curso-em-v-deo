p = float(input('Qual é o salario do funcionario? R$:'))

d = p + (p * 15 / 100)

print("O funcionario ganhava R$ {:.2f}, com 15% de aumento, passa a receber {:.2f}".format(p, d))
