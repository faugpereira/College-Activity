#C = (F - 32) /1.8

f = int(input('\nDigite a temperatura em Fahrenheit para descobrir qual será sua correspondência em Celsius: '))

c = (f-32)/1.8

print('\n',f,'ºF corresponde a',c,'ºC')

c1 = int(input('\nDigite a temperatura em Celsius para descobrir qual será sua correspondência em Fahrenheit: '))

f1 = c1 * 1.8 + 32

print('\n',c1,'ºC corresponde a',f1,'ºF')