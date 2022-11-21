valor_casa = float(input('Qual o valor do imóvel?'))
salario = float(input('Qual seu salário?'))
anos = int(input('Em quantos anos pretende pagar o empréstimo?'))

prestacao_mensal = valor_casa / (anos * 12)

print('O valor da prestação mensal é de R${:.2f}.'.format(prestacao_mensal))

if prestacao_mensal < (salario*0.3):
    print('Empréstimo aprovado!')
else:
        print('Empréstimo negado.')
