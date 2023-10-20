
temporario=[]
principal=[]
maior=menor=qtd=0
print("Digite os dados solicitados a seguir:")

while True:
    temporario.append(str(input("Nome: ")))
    temporario.append(float(input('Peso: ')))
    if len(principal)==0:
        menor=maior=temporario[1]
    else:
        if temporario[1]>maior:
            maior=temporario[1]
        if temporario[1]<menor:
            menor=temporario[1]

    principal.append(temporario[:])
    temporario.clear()
    while True:
        opcao=str(input('Deseja adicionar mais pessoas?[S/N]')).strip().upper()[0]
        if opcao=='S' or opcao=='N':
            break
        else:
            print("Escolha inválida. Digite 'S' ou 'N' para continuar.")

    if opcao=='N':
        break


print(f"Foram incluídas {len(principal)} pessoas." if len(principal)>1 else f"Foi incluída {len(principal)} pessoa.")
print(f"O maior peso digitado foi {maior:.1f} referente à ",end='')
for p in principal:
    if p[1]==maior:
        print(f"[{p[0]}] ",end='')

print(f"\nO menor peso digitado foi {menor:.1f}.")