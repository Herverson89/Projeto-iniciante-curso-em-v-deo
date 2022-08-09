vc = 60
km = 0.15
al= int(input('para quantos dias voce quer alugar: '))
pp= int(input("quantos km voce percorreu: "))

vf = (vc*al) + (pp*km)

print(vf)

##forma simplificada

dias= int(input('Quantos dias alugados? '))
km= int(input("quantos km voce rodados? "))
pago = (dias * 60) + (km * 0.15)
print(f'o total a pagar é de R${pago:.2f}')