from math import sqrt
co = float(input('Digite o valor do cateto oposto:'))
ca = float(input('Digite o valor do cateto adjacente:'))
h = sqrt(co**2 + ca**2)
print('Se o cateto oposto é {} e o cateto adjacente é {}, a hipotenusa é {}'.format(co, ca, h))

# uma possível melhoria seria não permitir valores negativos para a entrada de valores. Outra possível melhoria seria impor regras de existência de triangulo ...
#... por mais que para triangulos retangulos essas regras não façam sentido (já que o co e o ca sendo positivos, o triangulo retangelo já existe).
