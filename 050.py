s = 0
print("Somarei apenas os pares, ok?")
for c in range(1,7):
    x = int(input("Digite o {}° número:".format(c)))
    if x % 2 == 0:
        s += x
print("A soma dos números pares que você digitou é {}.".format(s))
