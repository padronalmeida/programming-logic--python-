n = float(input('Digite um número natural:'))

if (n <= 0) or ((n>0) and (n%1 != 0)):
    print('Os números naturais são os inteiros maiores que zero!')
else:
    if (n%2 == 0):
        print('Esse número é par!')
    else:
        print('Esse número é ímpar!')
