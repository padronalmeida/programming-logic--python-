n = 0
s = 0

while True:
    n = int(input('Digite um número:'))
    if n != 999:
        s = s + n
    else:
        print(f'A soma de todos os números que você digitou é {s}.')
        break
