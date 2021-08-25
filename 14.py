#Volume = 3.1416 * R2 * Altura

r = int(input('\nDigite o raio: '))

h = int(input('\nDigite a altura: '))

v = 3.1416 * r**2 * h

print('\nO volume de um objeto com',r,'cm de raio e',h,'cm de altura é',v,'cm³')