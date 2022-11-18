import math
ag = float(input('Digite um ângulo e veja seu seno, cosseno e tangente:'))
ar = math.radians(ag)
print('O seno de {} é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}.'.format(ag, math.sin(ar), math.cos(ar), math.tan(ar)))
