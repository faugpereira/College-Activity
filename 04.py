s = int(input('Insira seu salário para descobrir quanto receberá após o reajuste: '))

if (s <= 1000) and (s >= 500):
    s += s * 15/100
    print('Seu salário receberá reajuste de 15% e será R$ {}'.format(s))
elif s > 1000:
    s += s * 5/100
    print('Seu salário receberá reajuste de 5% e será R$ {}'.format(s))