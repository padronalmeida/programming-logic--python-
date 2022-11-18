import random, math

num_s = random.randint(1, 5)

num_e = float(input("Digite um número inteiro de 1 a 5:"))

if ((num_e // 1) != num_e):
    print('Esse número não é inteiro!')
else:
    if (num_e > 5) or (num_e < 1):
        print('Esse número não está entre 1 e 5 (inclusos)')
    else:
        if num_e == num_s:
            print("""
            Parabéns! Você tinha 20% de chances de acertar
            e você acertou! O número sorteado foi {}!
            """.format(num_s))
        else:
            print("""
            Você errou - o número que você escolheu foi {}
            e o número sorteado foi {}. Tente novamente, caso deseje.
            """.format(num_e, num_s))
