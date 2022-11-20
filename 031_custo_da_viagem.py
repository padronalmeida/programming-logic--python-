dist_viagem = float(input('Digite a distância da sua viagem em kilometros:'))
if dist_viagem < 0:
    print('A distância precisa ser maior que zero!')
else:
    if dist_viagem <= 200:
        preço_viagem = (dist_viagem * 0.50)
        print('A viagem custará R${}.'.format(preço_viagem))
    else:
        preço_viagem = (dist_viagem * 0.45)
        print('A viagem custará R${}.'.format(preço_viagem))
