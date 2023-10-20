lista=[]

while True:
    numero=int(input("Adicione um número a lista:"))
    if numero not in lista:
        lista+=[numero,]
    while True:
        opcao=str(input("Deseja adicionar mais algum número?(S/N)")).strip().upper()
        if opcao=='S':
            break
        elif opcao=='N':
            break
        else:
            print("Opção inválida. Tente novamente.")
    if opcao=='N':
        break
print(sorted(lista))
