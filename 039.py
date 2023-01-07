ano_de_nascimento = int(input('Digite o ano de seu nascimento (com 4 dígitos):'))
idade = 2023 - ano_de_nascimento

if idade < 18:
    print("Ainda não chegou o momento de se colocar à disposição da pátria!")
    tempo_para_servir = 18 - idade
    print("Você deverá se alistar daqui a {} anos.".format(tempo_para_servir))
elif idade == 18:
    print("Você deve se alistar esse ano!")
else:
    print("Já passou da hora de você se alistar!")
    tempo_para_ter_servido = idade - 18
    print("Você deveria ter se alistado há {} anos.".format(tempo_para_ter_servido))
    
