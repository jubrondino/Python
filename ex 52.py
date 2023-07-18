
numero=int(input("Digite um número para verificarmos se ele é primo:"))
soma=0

for dividendo in range(1,numero+1):
    if numero%dividendo==0:
        soma+=dividendo

if soma==numero+1:
    print(f"{numero} é primo.")
else:
    print(f"{numero} não é primo.")

