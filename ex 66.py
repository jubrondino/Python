contador=0
multiplicacao=1
while True:
    numero=int(input("Digite um número que deseja saber a tabuada: "))
    print("Se não quiser saber mais nenhuma tabuada digite um número negativo.")

    if numero>=0:
        for contador in range(0,11):
            multiplicacao=contador*numero
            print(f"{contador} x {numero} = {multiplicacao}")

    else:
        print("FIM")
        break

