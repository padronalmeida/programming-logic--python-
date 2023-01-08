
while True:
    a = float(input('Digite sua primeira nota:'))
    b = float(input('Digite sua segunda nota:'))
    if ((a+b)/2) >= 0 and ((a+b)/2) < 5:
        print("Sua média é {}. Você está reprovado.".format((a+b)/2))
        break
    elif ((a+b)/2) >= 5 and ((a+b)/2) < 7:
        print("Sua média é {}. Você tem direito à recuperação.".format((a+b)/2))
        break
    elif ((a+b)/2) >= 7 and ((a+b)/2) <= 10:
        print("Sua média é {}. Você foi aprovado!".format((a+b)/2))
        break
    elif ((a+b)/2) >= 10:
        print("Sua média é maior que 10? Acredito que tenha digitado errado. Digite as notas novamente.")
    else:
        print("Acredito que você tenha digitado errado. Digite as notas novamente.")
