quantidade_mulher_menor20=quantidade_maior18=quantidade_homem=0

while True:
    print("="*30)
    print("Cadastro de usuário")
    print("="*30)
    nome=str(input("Nome: "))
    idade=int(input("Idade: "))
    sexo=' '
    while sexo not in 'FM':
        sexo = str(input("Sexo[F/M]: ")).strip().upper()[0]

    opcao=' '
    while opcao not in 'SN':
        opcao = str(input("Deseja cadastrar mais usuários?[S/N]: ")).strip().upper()[0]
    if opcao=='N':
        break
    if sexo=='M':
        quantidade_homem+=1
    if idade>18:
        quantidade_maior18+=1
    if idade<20 and sexo=='F':
        quantidade_mulher_menor20+=1
print(f"""
Programa finalizado.
Foram cadastrados:
{quantidade_homem} pessoas(s) do sexo masculino.
{quantidade_maior18} pessoa(s) maior(es) de 18 anos.
{quantidade_mulher_menor20} mulher(es) com menos de 20 anos.
""")

