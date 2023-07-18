while True:
    preco_str=str(input("Preço do produto: "))
    preco_str=preco_str.replace(',','.')
    preco=float(preco_str)

    if preco<=0:
        print("Por favor, digite um preço válido.")

    else:
        break

while True:
    opcao=int(input("""

**************ESCOLHA A FORMA DE PAGAMENTO**************

            [1] À VISTA NO DINHEIRO
            [2] À VISTA NO CARTÃO
            [3] 2x NO CARTÃO
            [4] 3x + NO CARTÃO
            
            OPÇÃO ESCOLHIDA:"""))
    print("********************************************************")

    if opcao==1:
        preco=preco*0.9
        print(f"\nValor a ser pago: R${preco:.2f}.\nVocê ganhou 10% de desconto.")
        break

    elif opcao==2:
        preco=preco*0.95
        print(f"\nValor a ser pago: R${preco:.2f}.\nVocê ganhou 5% de desconto.")
        break

    elif opcao==3:
        print()
        print(f"\nO valor a ser pago: R${preco:.2f}.\nValor sem descontos.")
        break

    elif opcao==4:
        preco=preco*1.2
        print(f"\nO valor a ser pago: R${preco:.2f}.\nValor com 20% de juros.")
        break

    else:
        print("\nPor favor, insira uma opção válida.\n")