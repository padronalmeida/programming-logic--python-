valores = []

for c in range (1,6):
    valores.append(float(input(f'Digite o {c}° valor:')))

valores_fixo = valores[:]
print(valores)

valores.sort()
em_ordem = valores[:]

valores.sort(reverse = True)
em_ordem_inversa = valores[:]

print(em_ordem)

print(em_ordem_inversa)

pos_men = valores_fixo.index(em_ordem[0]) + 1
print(em_ordem[0])

pos_maior = valores_fixo.index(em_ordem[-1]) + 1
print(em_ordem[-1])

print(f'O menor valor da lista é o {em_ordem[0]} e foi o {pos_men}° a ser digitado. O maior valor é o {em_ordem[-1]} e foi o {pos_maior}° valor a ser digitado')
