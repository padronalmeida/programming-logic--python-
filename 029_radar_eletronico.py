vel_r = float(input('Digite a velocidade que o carro passou:'))

if vel_r <= 0:
    print("Não existe velocidade negativa, irmão!")
else:

    vel_l = float(input('Digite a velocidade limite:'))

    if vel_l <= 0:
        print("O limite de velocidade tem que ser positivo, irmão!")
    else:

        rs_multa = (vel_r - vel_l) * 7

        if (vel_r <= vel_l):
            print("Você não foi multado.")
        else:
            print("""
            O limite de velocidade era de {}km/h
            e você passou no radar a {}km/h.
            Você foi multado em R${:.2f}
            """.format(vel_l, vel_r, rs_multa))
