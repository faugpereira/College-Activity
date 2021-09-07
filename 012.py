n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
n3 = int(input('Digite a terceira nota: '))

m = ((n1*2)+(n2*3)+(n3*5))/10

print('Sua média foi {}'.format(m))

if m>=8 and m<=10:
    print('Classificação A')
elif m>=7 and m<8:
    print('Classificação B')
elif m>=6 and m<7:
    print('Classificação C')
elif m>=5 and m<6:
    print('Classificação D')
else:
    print('Classificação R')