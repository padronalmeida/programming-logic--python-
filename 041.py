idade = 2023 - int(input("Digite o ano de nascimento do atleta:"))

while idade <=0:
    print("O atleta precisa ter nascido no máximo em 2022.")
    idade = 2023 - int(input("Digite o ano de nascimento do atleta:"))

if 0 < idade < 9:
    print("MIRIM")
elif 9 <= idade < 14:
    print("INFANTIL")
elif 14 <= idade < 19:
    print("JUNIOR")
elif 19 <= idade < 25:
    print("SÊNIOR")
else:
    print("MASTER")
