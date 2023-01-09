# números por extenso
nos_ext = ("um","dois","três","quatro","cinco")

#possíveos escolhas:
nos = (1,2,3,4,5)

#escolha inicial só para entrar no laço
nos_esc = 0

#enquanto o usuário não escolher 1, 2, 3, 4 ou 5 ele não sai do laço
while nos_esc not in nos:
     nos_esc = int(input("Digite um número entre 1 e 5:"))

    
print(f'Você digitou o número {nos_ext[nos_esc - 1]}.')
