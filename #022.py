#funçao strip é usado par eliminar os espaços no inicio e no final,
#para eliminar o espaço entre as letras e necesario usar outra função


nome = str(input('Digite seu nome completo: ')).strip()
nome1 = len(nome) - nome.count(' ')
nome2 = nome.find(' ')
print(f"Seu nome completo em maiuscula é : ", nome.upper())
print(f"Seu nome completo em minuscula é : ", nome.lower())
print(f"Seu nome tem {nome1} letras ")
print(f"Seu nome primeiro nome tem {nome2} letras ")