from random import randint

vitoria=soma=0
escolha=''

print("=-"*30)
print("Vamos jogar par ou impar!")
print("=-"*30)


while True:
    num_jogador=int(input("Digite um número: "))
    escolha = str(input("Você quer par ou ímpar? [P/I]: ")).strip().upper()

    while escolha not in 'PI':
        escolha=str(input("Você quer par ou ímpar? [P/I]: ")).strip().upper()

    num_computador= randint(1,10)

    print(f"Eu joguei {num_computador} e você {num_jogador}.")

    soma=num_jogador+num_computador

    if escolha=='P':
        if soma%2==0:
            print(f"Parabéns.{soma} é par e você escolheu par. Você ganhou.\nVamos jogar novamente!\n\n")
            vitoria+=1
        else:
            print(f"Você perdeu. {soma} é ímpar e você escolheu par.\nNúmero de vitórias: {vitoria}.")
            break
    else:
        if soma%2!=0:
            print(f"Você ganhou.{soma} é ímpar e você escolheu ímpar.\nVamos jogar novamente.\n\n")
            vitoria+=1
        else:
            print(f"Você perdeu.{soma} é par e você escolheu ímpar.\nNúmero de vitórias: {vitoria}.")
            break