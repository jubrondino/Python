numero=int(input("Digite um número que deseja saber a tabuada:"))
resultado=0
for tabuada in range(0,11):
    resultado=numero*tabuada
    print(f"{numero} x {tabuada} = {resultado}")