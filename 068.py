import random

c = 0

while True:
    #Escolha do jogador
    poi = int(input("Par(0) ou ímpar(1)?"))
    
    #dedos do computador
    dc = random.randint(1,2)

    #números de dedo do jogador
    dj = int(input("Escolha quantos dedos mostrar:"))


    if ((dc + dj) % 2) == poi:
        c += 1
        print("Você ganhou, jogue novamente!")
    else:
        c += 1
        break

if poi == 1:
    nome_poi = 'ímpar'
else:
    nome_poi = 'par'

print("""Você mostrou {} dedos e o computador mostrou {} dedos.
Como tinha escolhido {}, você perdeu ! 
Você ganhou {} vezes até que o computador venceu você!""".format(dj, dc, nome_poi, c-1))
