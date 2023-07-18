from datetime import date

ano_atual=date.today().year
ano_nascimento=int(input("Ano de nascimento: "))
idade=ano_atual-ano_nascimento
print(f"O atleta tem {idade} anos.")

if idade<=9:
    print("Classificação: Mirim.")
elif idade <=14:
    print("Classificação: Infantil.")
elif idade<=19:
    print("Classificação: Junior.")
elif idade<=25:
    print("Classificação:Sênior.")
else:
    print("Classificação:Master.")
