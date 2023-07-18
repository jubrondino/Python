
soma_idade=0
soma_mulheres_menos20=0
maior_idade=0
homem_mais_velho=''

for contador in range(0,4):
    print(f"\nDados da {contador+1}º pessoa:")
    nome=str(input("Nome: "))
    idade=int(input("Idade: "))
    sexo_correto = False
    while not sexo_correto:
        sexo=input("""
        Escolha o sexo:
        [1] para Feminino 
        [2] para Masculino
        ->""")
        if sexo=='1' or sexo=='2':
            sexo_correto = True
        else:
            print("\nVocê precisa escolher a opção 1 ou 2 para definir o sexo.\n")


    if sexo==1 and idade<20:
        soma_mulheres_menos20+=1

    if idade>maior_idade and sexo=='2':
        maior_idade=idade
        homem_mais_velho=nome

    media=soma_idade/4
    soma_idade += idade


print(f"""
Há {soma_mulheres_menos20} mulheres com menos de 20 anos.
A média das idades é {media} anos.
O homem mais velho tem {maior_idade} anos e se chama {homem_mais_velho}.
""")