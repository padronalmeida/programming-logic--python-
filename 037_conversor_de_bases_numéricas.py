num = int(input('Digite um número inteiro qualquer:'))
escolha = int(input("""
Escolha para qual base quer converter o número digitado:
1 - binário;
2 - octal;
3 - hexadecimal
"""))

if escolha == 1:
    print('O número {} em binário é {}.'.format(num, bin(num)))
elif escolha == 2:
    print('O número {} em octal é {}.'.format(num, oct(num)))
elif escolha == 3:
    print('O número {} em hexadecimal é {}.'.format(num, hex(num)))
else:
    print('Opção inválida.')
