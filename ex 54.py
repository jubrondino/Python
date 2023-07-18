from datetime import datetime

ano_atual = datetime.now().year
soma = 0

for contador in range(0, 6):
    data_valida = False
    while not data_valida:
        ano_nascimento = int(input(f"Digite a data de nascimento da {contador+1}ª pessoa: "))

        if ano_nascimento < ano_atual - 105:
            print("Por favor, confira a data digitada e tente novamente.\n")
        else:
            data_valida = True

    if (ano_atual - ano_nascimento) > 18:
        soma += 1

print(f"\n{soma} pessoas são maiores de idade.")

