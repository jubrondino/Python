soma=0
quantidade=0


while True:
    numero=int(input("Digite um número: "))

    quantidade+=1
    soma+=numero

    if quantidade==1:
        maior=menor=numero
    else:
        if numero>maior:
            maior=numero
        if numero<menor:
            menor=numero

    opcao=str(input("Deseja inserir outro número?[S/N]\n>>>>")).strip().upper()

    if opcao=='N':
        break
    else:
        continue

media=soma/quantidade
print(f"A média é {media:.2f}, o menor número é {menor} e o maior número é {maior}. ")