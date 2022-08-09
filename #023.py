num = int(input('Digite um numero ate 4 caractere :'))

unidade = num // 1 %10
dezena = num // 10 %10
centena = num // 100 %10
milhar = num // 1000 %10


print(f'Analisando o número {num} ')
print(f'Unidade: {unidade} ')
print(f'Dezena : {dezena} ')
print(f'Centena: {centena} ')
print(f'milhar : {milhar} ')