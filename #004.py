a = input("Digite algo: ")
print('O tipo primitivo desse valor é: ', type(a))

print('Tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É um alfanumerico? ', a.isalnum())
print('É um alfabetico? ', a.isalpha())
print('Está em maiuscula? ', a.isupper())
print('Está em minuscula? ', a.islower())
print('Está em capitalizada? ', a.istitle())