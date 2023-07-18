"""while sexo=="F" or sexo=="M":
    sexo=str(input("Digite o sexo[F/M]:")).strip().upper()[0]
    print(f"Sexo {sexo} registrado com sucesso.")
    if sexo !="F" or sexo!="M":
        print("Por favor, digite o sexo novamente.")"""


sexo=str(input("Digite o sexo[F/M]:")).strip().upper()[0]
while sexo not in 'MF':
    sexo=str(input("Sexo inválido. Por favor, digite o sexo novamente:")).strip().upper()[0]

print(f"Sexo {sexo} registrado com sucesso.")