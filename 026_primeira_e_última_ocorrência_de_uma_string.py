frase = str(input('Digite sua frase:')).lower().strip().replace(' ', '')
n_a = frase.count('a')
pos_1 = int(frase.find('a'))
pos_1_ord = pos_1 + 1
pos_n = int(frase.rfind('a'))
pos_n_ord = pos_n + 1

print('Há {} as na frase. O primeiro sendo a {}a letra e o último sendo a {}a.'.format(n_a, pos_1_ord, pos_n_ord))
