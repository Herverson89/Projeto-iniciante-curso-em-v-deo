frase = str(input("Digite uma frase que contanha a letra (a): ")).upper().strip()

print("A frase digitada foi {},A quantidade de letras (a) digitadas foi {} vezes. ".format(frase, frase.count('A')))
print("A primeira letra (a) aparece na possição {} ".format(frase.find('A')))
print("E sua ultima possição é  {} ".format(frase.rfind('A')))