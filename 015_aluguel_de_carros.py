km = float(input('Digite quantos kms foram percorridos com o carro:'))
dias = int(input('Digite quantos dias ficou com o carro:'))
valor = (60*dias) + (0.15*km)
if (km <= 0) or (dias <= 0):
    print('Tanto o número de dias quanto a kilometragem precisam ser positivas.')
else:
    print('O valor do aluguel do carro será de R${:.2f}.'.format(valor))
