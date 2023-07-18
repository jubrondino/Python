from random import choice
from time import sleep

while True:

    print("*************** GAME: PEDRA // PAPEL // TESOURA ***************")

    escolha_usuario=str(input("Qual a sua escolha?\n-->"))
    escolha_usuario=escolha_usuario.upper()

    if escolha_usuario not in ["PAPEL","TESOURA","PEDRA"]:
        print("Opção inválida.\nPor favor, escolha entre PAPEL,PEDRA E TESOURA.\n\n")
    else:
        break

lista_opcoes=["PEDRA","PAPEL","TESOURA"]
escolha_pc= choice(lista_opcoes)
print(f"\nJokey PO")
sleep(1)
print(f"Você escolheu {escolha_usuario} e o computador escolheu {escolha_pc}.")


if escolha_usuario==escolha_pc:
    print("Empate. Tente novamente.")


elif escolha_usuario=="PEDRA" and escolha_pc=="TESOURA":
    print("Parabéns! Você ganhou.\nPedra destrói tesoura")


elif escolha_usuario=="PEDRA" and escolha_pc=="PAPEL":
    print("Que pena. Você perdeu.\nPapel embrulha pedra.")


elif escolha_usuario=="TESOURA" and escolha_pc=="PAPEL":
    print("Parabéns! Você ganhou.\nTesoura corta papel.")


elif escolha_usuario=="TESOURA" and escolha_pc=="PEDRA":
    print("Que pena. Você perdeu.\nPedra destrói tesoura.")


elif escolha_usuario=="PAPEL" and escolha_pc=="PEDRA":
    print("Parabéns! Você ganhou.\nPapel embrulha pedra.")


elif escolha_usuario=="PAPEL" and escolha_pc=="TESOURA":
    print("Que pena. Você perdeu.\nTesoura corta papel.")




