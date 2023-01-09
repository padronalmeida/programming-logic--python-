a = float(input("Digite a reta 1:"))
while a <= 0:
    print("O tamanho da reta precisa ser maior que zero.")
    a = float(input("Digite a reta 1:"))

b = float(input("Digite a reta 2:"))
while b <= 0:
    print("O tamanho da reta precisa ser maior que zero.")
    b = float(input("Digite a reta 2:"))

c = float(input("Digite a reta 3:"))
while c <= 0:
    print("O tamanho da reta precisa ser maior que zero.")
    c = float(input("Digite a reta 3:"))

if (a+b) <= c or (a+c) <= b or (b+c) <= a:
    print("Esses três segmentos de reta não podem formar um triângulo.")
else:
    print("Os três segmentos de reta formam um triângulo.") 
