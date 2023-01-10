e = 's'
valores = []
c = 0
while True:
    if e == 's':
        x = int(input('Digite um valor:'))
        if x not in valores:
            valores.insert(c, x)
        else:
            print(f'O número {x} já fazia parte da lista e não será adicionado novamente.')
        e = input('Quer continuar?(S/N').lower()
        c += 1
    if e == 'n':
        break

valores.sort()
print(valores)
