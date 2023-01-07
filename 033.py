a = int(input("Digite o primeiro número:"))
b = int(input("Digite o segundo número (diferente do primeiro):"))
c = int(input("Digite o terceiro número (diferente do primeiro e do segundo):"))

if a > b and a > c:
    print("O primeiro número é o maior dos três.")
    if b > c:
        print("O terceiro número é o menor.")
    else:
        print("O segundo número é o menor.")
elif b > a and b > c:
    print("O segundo número é o maior dos três.")
    if a > c:
        print("O terceiro número é o menor.")
    else:
        print("O primeiro número é o menor.")
else:
    print("O terceiro número é o maior dos três.")
    if b > a:
        print("O primeiro número é o menor.")
    else:
        print("O segundo número é o menor.")
