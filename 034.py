s = int(input("Qual seu salário?"))

if s <= 1250:
    print("""Seu aumento será de {} por cento do seu salário, o que equivale a R${}.
    Sendo assim, seu novo salário será de {}.""".format(15, s*0.15,s*1.15))
else:
    print("""Seu aumento será de {} por cento do seu salário, o que equivale a R${}.
    Sendo assim, seu novo salário será de {}.""".format(10, s*0.1,s*1.1))
