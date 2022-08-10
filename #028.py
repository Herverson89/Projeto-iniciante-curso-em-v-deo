from random import randint # de random importamos a função randint ela eslhore randomicamente o que foi declarado.
from time import sleep # de time importamos a função sleep ela conta os sec par processar a proximo comando.
print("\033[0;49;31m-=\033[m"*20)
print("\033[0;49;34mPense em um numero de 0 a 5\033[m")
print("\033[0;49;31m-=\033[m"*20)

#EXTRA: É possivel mudar a cor das letras
computador = randint(0, 5) #utiliza a função importada randint ela faz com que o computador escolha numeros aleatorios de 0 a 5
jogador = int(input("\033[0;49;34mDigite um numero que pensou: \033[m"))

print("\033[0;49;34mProcessando!!!\033[m")
sleep(3)
if jogador == computador:
    print("\033[0;49;34mParabéns você acertou o numero!!!\033[m")


else:
    print('\033[0;49;34mNão foi desta vez, eu pensei no numero {}, e você pensou {}, você perdeu!!\033[m'.format(computador, jogador))
