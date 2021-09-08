n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
n3 = int(input('Digite a terceira nota: '))

m = ((n1*2)+(n2*3)+(n3*5))/10

print('Sua média foi {}'.format(m))

if m>=8 and m<=10:
    print('\033[0;34mClassificação A\033[m')
elif m>=7 and m<8:
    print('\033[0;36mClassificação B\033[m')
elif m>=6 and m<7:
    print('\033[0;33mClassificação C\033[m')
elif m>=5 and m<6:
    print('\033[0;35mClassificação D\033[m')
else:
    print('\033[0;31mClassificação R\033[m')