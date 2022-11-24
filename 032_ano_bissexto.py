ano = int(input("Digite um ano - com quatro dígitos - e descubra se trata-se de um ano bissexto:"))

if (((ano - 2000)%4) == 0):
    print(f'O ano de {ano} é bissexto!')
else:
    print(f'O ano de {ano} não é bissexto.')
