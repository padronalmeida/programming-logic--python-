import random

contador = 0

while True:
    contador = contador + 1
    escolha_jogador_par_ou_impar = str(input("\n"
                                             "\"Par ou ímpar?\n"
                                             "[A] Par\n"
                                             "[B] Ímpar\n")).lower()
    escolha_jogador_dedos = int(input("Escolha quantos dedos mostrar."))
    escolha_computador_dedos = random.randint(1, 2)
    if escolha_jogador_par_ou_impar == 'a':
        if (((escolha_jogador_dedos + escolha_computador_dedos)%2) == 0):
            print(f"""
    O computador mostrou {escolha_computador_dedos} dedo(s) e você mostrou {escolha_jogador_dedos} dedo(s).
    Deu par! Você venceu!
            """)
        else:
            print(f"""
    O computador mostrou {escolha_computador_dedos} dedo(s) e você mostrou {escolha_jogador_dedos} dedo(s).
    Deu ímpar! Você perdeu após {contador} rodada(s)!
            """)
            break

    else:
        if (((escolha_jogador_dedos + escolha_computador_dedos) % 2) != 0):
            print(f"""
        O computador mostrou {escolha_computador_dedos} dedo(s) e você mostrou {escolha_jogador_dedos} dedo(s).
        Deu ímpar! Você venceu!
                """)
        else:
            print(f"""
        O computador mostrou {escolha_computador_dedos} dedo(s) e você mostrou {escolha_jogador_dedos} dedo(s).
        Deu par! Você perdeu após {contador} rodada(s)!
                """)
            break
