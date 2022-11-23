import random

num_esc = int(input("Tente advinhar qual número inteiro de 0 a 10 o computador sorteou:"))
num_sor = random.randint(1,10)
cont = 0

while num_esc != num_sor:
    cont = cont + 1
    num_esc = int(input("Você errou e essa é sua {} tentativa. Tente novamente.".format(cont)))

num_esc = int(input("Você precisou de {} tentativas, mas você acertou! O número é o {}.".format(cont, num_sor)))
