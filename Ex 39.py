from datetime import date

ano_nascimento=int(input("Digite o ano em que você nasceu: "))
ano_atual=date.today().year
idade=ano_atual-ano_nascimento
ano_alistamento=ano_nascimento+18

if idade>18:
    print(f"\nVocê tem {idade} anos.Atenção você já deveria ter se alistado em {ano_alistamento}.")

elif idade==18:
    print("\nVocê completou/completará 18 anos nesse ano. Aliste-se imediatamente.")

else:
    print(f"\nVocê tem {idade} anos e ainda não atingiu a maioridade.\nSeu alistamento será em {ano_alistamento}.")