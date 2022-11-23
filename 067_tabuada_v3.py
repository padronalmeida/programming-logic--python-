n = int(input('Digite a tabuada de qual número quer ver:'))

while True:

    if n > 0:
        print(f'{n} vezes 1 = {n * 1}')
        print(f'{n} vezes 2 = {n * 2}')
        n = int(input('Digite a tabuada de outro número que queira ver:'))
    else:
        print('Acabou.')
        break
