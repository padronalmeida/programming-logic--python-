
#soma = 0

#for c in range(3,500,6):
#    soma += c
#    print(c)
#    print(soma)
#print(soma)

soma = 0

for c in range(1,501,1):
    if c % 3 == 0 and c % 2 != 0:
        soma += c
    print(c)
    print(soma)
