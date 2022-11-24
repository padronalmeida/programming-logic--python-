n1 = int(input(f'Digite o primeiro número:'))
n2 = int(input(f'Digite o segundo número:'))
escolha = 0

while escolha != 5:
    escolha = int(input(f"""
    Você escolheu os números {n1} e {n2}.
    Digite a opção desejada:
    1 somar
    2 multiplicar
    3 dizer quem é o maior
    4 escolher novos números
    5 encerrar programa
        """))
    if escolha == 1:
        print(f'A soma de {n1} e {n2} é {n1 + n2}.')
    elif escolha == 2:
        print(f'O produto de {n1} e {n2} é igual a {n1 * n2}')
    elif escolha == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}.')
        elif n2 > n1:
            print(f'{n2} é maior que {n1}.')
        else:
            print(f'{n1} e {n2} são iguais.')
    elif escolha == 4:
        n1 = int(input(f'Digite o primeiro número:'))
        n2 = int(input(f'Digite o segundo número:'))
    elif escolha == 5:
        print('Obrigado por usar nosso programa.')
    else:
        print('Escolha uma das opções disponíveis.')
