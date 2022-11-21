largura = float(input('Digite a largura da parede (em metros):'))
altura = float(input('Digite a altura da parede (em metros):'))
area = largura * altura
litros = area / 2

print('Para pintar uma parede de {} m² você precisará de {} litros de tinta.'.format(area, litros))
