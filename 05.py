n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))

menor = n1
if (menor > n2):
    menor = n2
    if menor > n3:
        menor = n3

maior = n1
if (maior < n2):
    maior = n2
    if maior < n3:
        maior = n3

meio = n1
if menor < n2 < maior:
    meio = n2
elif menor < n3 < maior:
    meio = n3

print('\n[{},{},{}]'.format(menor, meio, maior))