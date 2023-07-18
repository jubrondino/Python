from random import randint
tentativa=0
print("Vou pensar num número de 1 a 10 e você tem que adivinhar qual número eu pensei. ")
escolha_pc=randint(1,10)
escolha_usuario=int(input("Que número eu pensei?\n"))


while escolha_pc!=escolha_usuario:

    tentativa+=1
    if escolha_pc<escolha_usuario:
        print("Menos..")
    else:
        print("Mais...")
    escolha_usuario=int(input("Tente novamente.\n"))

print(f"Eu pensei em {escolha_pc}.\nVocê acertou com {tentativa} tentativas.")
