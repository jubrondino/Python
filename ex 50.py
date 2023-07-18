soma=0
for numeros in range(0,6):
    num=int(input(f"Digite o {numeros+1}º número: "))
    if num%2==0:
        soma+=num
print(f"A soma dos números pares digitados é {soma}.")
