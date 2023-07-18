print("""
***************************************************
              LOJA SUPER BARATÃO
***************************************************

""")
soma = produtos_maior1000 = quantidade_produtos = 0
produto_barato = ''
mais_barato = float('inf')

while True:
    produto = input("Digite o nome do produto: ")
    preco = input("Digite o preço do produto: ")
    novo_preco = float(preco.replace(",", "."))
    soma += novo_preco


    if novo_preco > 1000:
        produtos_maior1000 += 1

    if novo_preco < mais_barato:
        mais_barato = novo_preco
        produto_barato = produto

    opcao = ' '
    while opcao not in 'SN':
        opcao = input("Deseja continuar? [S/N]: ").strip().upper()[0]
    if opcao == 'N':
        break

print(f"""
            SALDO:
TOTAL: {soma}
PRODUTO MAIS BARATO: {produto_barato}
QUANTIDADE DE PRODUTOS QUE CUSTAM MAIS DE 1000 REAIS: {produtos_maior1000}

""")
