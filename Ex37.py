
numero=int(input("Digite o número que deseja converter:"))

while True:

    opcao=int(input("""Para qual deseja converter:

                1 para binário
                2 para octal
                3 para hexadecimal
                
               Escolha sua opção: """))

    if opcao==1:
        print(f"\nO número {numero} em binário é {bin(numero)[2:]}")
        break

    elif opcao==2:
        print(f"\nO número {numero} em octal é {oct(numero)[2:]}")
        break

    elif opcao==3:
        print(f"\nO número {número} em octal é {hex(numero)[2:]}")
        break
    else:
        print("\n\aOpção inválida.\nEscolha uma opção válida.\n")
