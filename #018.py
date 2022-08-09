from math import radians, sin, cos, tan
angulo = float(input('digite o andulo que vocë deseja: '))
seno = sin(radians(angulo))
print('O angulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('o angulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))