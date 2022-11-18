nome = input('Digite seu nome:').strip()
nome_maiusculo = nome.upper()
nome_minusculo = nome.lower()
nome_sem_espacos = nome.replace(" ","")
posicao_primeiro_espaço = nome.find(" ")
tamanho_primeiro_nome = len(nome[0:posicao_primeiro_espaço])
print("""
{}, todo em maiúsculo é {},
todo em minúsculo é {},
o nome comleto - desconsiderando os espaços - tem {} letras e
o primeiro nome tem {} letras.
""".format(nome, nome_maiusculo, nome_minusculo, len(nome_sem_espacos), tamanho_primeiro_nome))
