n = int(input('Digite um número: '))

a = 10
b = 25
c = 20
d = 30

if (n>=a) and (n<=b):
    if (n>=c) and (n<=d):
        print('O número {} está dentro dos intervalos [{},{}] e [{},{}]'.format(n, a, b, c, d))
    else:
        print('O número {} está dentro do intervalo [{},{}]'.format(n, a, b))
elif (n>=c) and (n<=d):
    print('O número {} está dentro do intervalo [{},{}]'.format(n, c, d))
else:
    print('O número {} está fora dos intervalos [{},{}] e [{},{}]'.format(n, a, b, c, d))