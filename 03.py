n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
n3 = int(input('Digite mais um número inteiro: '))

if (n1 > n2) and (n1 > n3):
    print('O número {} é o maior.'.format(n1))
elif (n2 > n1) and (n2 > n3):
    print('O número {} é o maior.'.format(n2))
else:
    print('O número {} é maior.'.format(n3))