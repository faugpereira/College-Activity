n = int(input('\nDigite um número com 4 digitos: '))

m = n//1000
r = n%1000

c = r//100
r = r%100

d = r//10

u = r%10

print('\nO digito referente ao milhar é: ',m,'\nO dígito referente à centena é: ',c,'\nO dígito referente à dezena é: ',d,'\nO dígito referente à unidade é: ',u)