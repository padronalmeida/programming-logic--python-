s = str(input("Qual seu sexo?")).lower().strip()

while (s != 'm') and (s != 'f'):
    s = str(input("Digite 'm' ou 'f':")).lower().strip()

print('Você é {}.'.format(s))
