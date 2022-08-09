import random
n1 = str(input('Digite um nome : '))
n2 = str(input('Digite um nome : '))
n3 = str(input('Digite um nome : '))
n4 = str(input('Digite um nome : '))
n5 = str(input('Digite um nome : '))

l1 = [n1, n2, n3, n4, n5]
random.shuffle(l1)

print(l1)
# importando a biblioteca random
# e utilizando a função shuffler ( embaralhar)
# foi poissivel embaralhar a lista