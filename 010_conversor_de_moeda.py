qtdd_cart_rs = float(input('Digite quantos reais tem na carteira:'))
qtdd_cart_usd = qtdd_cart_rs / 5.33
usd = qtdd_cart_usd // 1
cents = qtdd_cart_usd % 1

if qtdd_cart_rs == 0:
    print('Desculpe a indelicadeza, mas você não tem dinheiro na carteira.')
else:
    if (usd == 0):
        print('Você tem {:.0f} cents na carteira.'.format(cents*100))
    else:
        if (usd == 1):
            print('Você tem 1 dólar e {:.0f} cents na carteira.'.format(cents*100))
        else:
            if (qtdd_cart_rs < 0):
                print('Não é possível ter um valor negativo na sua carteira FÍSICA.')
            else:
                print('Você tem {:.0f} dólares e {:.0f} cents na carteira.'.format(usd, cents*100))
