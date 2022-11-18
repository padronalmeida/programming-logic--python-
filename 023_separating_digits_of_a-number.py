num = int(input("Digite um número de 0 a 9999:"))

#melhoria aqui é colocar condição automática de conferência

u_num = num % 10
d_num = (num // 10) % 10
c_num = (num // 100) % 10
m_num = (num // 1000) % 10

print("A unidade é {}.".format(u_num))
print("A dezena é {}.".format(d_num))
print("A centena é {}.".format(c_num))
print("A milhar é {}.".format(m_num))

# segunda melhoria, fazer isso para qualquer número digitado.
