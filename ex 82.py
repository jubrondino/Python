lista=[]
lista_par=[]
lista_impar=[]

while True:
    numero=int(input("Digite um número:"))
    lista.append(numero)
    while True:
        opcao=str(input("Deseja digitar outro número?[S/N]")).strip().upper()
        if opcao=='S' or opcao=='N':
            break
        else:
            print("Opção inválida. Digite novamente.")
    if opcao=='N':
        break

for c in lista:
    if c%2==0:
        lista_par.append(c)
    else:
        lista_impar.append(c)

print(f"A lista original é {lista}.")
print(f"A lista de números pares é {lista_par}.")
print(f"A lista de números ímpares é {lista_impar}.")