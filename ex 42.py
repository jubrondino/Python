print("Intuito do programa é verificar se 3 valores podem ou não formar um triângulo e qual tipo de triângulo.")
while True:

    lado1=float(input("Digite o primeiro lado: "))
    lado2=float(input("Digite o segundo lado: "))
    lado3=float(input("Digite o terceiro lado: "))

    if lado1<=0 or lado2<=0 or lado3 <=0:
        print("\nPara formar um triângulo nenhum lado pode ser menor ou igual a 0.\nTente novamente.\n")

    elif lado1+lado2>lado3 and lado2+lado3>lado1 and lado3+lado1>lado2:
        print("\nAs medidas formam um triângulo", end='')

        if lado1==lado2 and lado2==lado3:
            print(" e o triângulo é equilátero.")

        elif lado1==lado2 and lado2!=lado3:
            print(" e o triângulo é isósceles.")

        else:
            print(" e o triângulo é escaleno.")
        break
    else:
        print("\nAs medidas não formam um triângulo.\nTente novamente.\n")