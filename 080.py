lista = []

for c in range(0,5):
    x = int(input("Cadastre um número inteiro:"))
    if c == 0 or x > lista[-1]:
        lista.append(x)
    else:
        pos = 0
        while pos < len(lista):
            if x <= lista[pos]:
                lista.insert(pos, x)
                break
            pos += 1
print(f'Os valores digitados, em ordem, foram {lista}.')