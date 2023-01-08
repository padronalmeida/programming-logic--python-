a = int(input("Digite um número inteiro positivo qualquer e veja seu fatorial:"))
b = a
fat = a

while True:
    if a > 1:
        fat = fat * (a-1)
        a = a - 1
    elif a == 1:
        print("O fatorial do número digitado {} é {}.".format(b,fat))
        break
    elif a == 0:
        print("O fatorial de 0 é 1.")
        break
    else:
        print("Não existe fatorial de número negativo.")
        break
