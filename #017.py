
#maneira de matematica simples sem importação
# co = float(input('comprimento do cateto oposto: '))
# ca = float(input('comprimento do cateto oposto: '))
# hi = (co** 2 + ca **2) ** (1/2)
# print('A hipotenusa vai medir  {:.2f}'.format(hi))




from math import hypot
co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto oposto: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir  {:.2f}'.format(hi))