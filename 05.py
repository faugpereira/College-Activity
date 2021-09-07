n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))

maior = -100000000
if (maior < n1):
    maior = n1
if (maior < n2):
    maior = n2
if (maior < n3):
    maior = n3

menor = 100000000
if (menor > n1):
    menor = n1
if (menor > n2) :
    menor = n2
if (menor > n3):
    menor = n3

meio = 0
if (n1 != maior and n1 != menor ):
    meio = n1
elif (n2 != maior and n2 != menor):
    meio = n2
else:
    meio = n3

print('[{},{},{}]'.format(menor, meio, maior))