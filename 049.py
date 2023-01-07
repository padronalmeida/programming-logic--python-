x = int(input("Digite um número e veja sua taboada até o 20."))

for c in range (1,21,1):
    t = c * x
    print("{} * {} = {}".format(x, c, t))
print("É isso aí!")
