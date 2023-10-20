lista=[]

while True:
    numero=int(input("Digite um número:"))
    lista+=[numero,]

    while True:
        opcao=str(input("Deseja digitar outro número?[S/N]:")).strip().upper()

        if opcao=='S' or opcao=='N':
            break
        else:
            print("Digite uma opção válida.")

    if opcao=='N':
        break

print(f"Foram digitados {len(lista)} números.")

lista.sort(reverse=True)

print(f"A lista em ordem descrecente é",end=' ')

for i,c in enumerate(lista):
    print(c, end=',' if i<len(lista)-2 else ' e ' if i==len(lista)-2 else '.')

if 5 in lista:
    print("\nO número 5 esta na lista e se encontra na(s) posição(ões): ",end='')
    for i, c in enumerate(lista):
        if c==5:
            print(f"{i+1}",end='  ')
else:
    print("\nO número 5 não está na lista.")