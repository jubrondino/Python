from sys import exit

num1=int(input("Digite um número:"))
num2=int(input("Digite outro número:"))

while True:
    opcao=int(input("""
                      MENU
                      
                      [1] SOMA
                      [2] MULTIPLICA
                      [3] MAIOR
                      [4] NOVOS NÚMEROS
                      [5] SAIR DO PROGRAMA  
                      >>>Qual sua opção?   
                      """))
    if opcao==1:
        soma=num1+num2
        print(f"A soma de {num1} + {num2} é {soma}.")

    elif opcao==2:
        multiplica=num1*num2
        print(f"A multiplicação de {num1}*{num2} é {multiplica}")

    elif opcao==3:
        if num1>num2:
            print(f"{num1} é maior que {num2}.")
        else:
            print(f"{num2} é maior que {num1}.")

    elif opcao==4:
        num1 = int(input("Digite um número:"))
        num2 = int(input("Digite outro número:"))
    elif opcao==5:
        print("Até a próxima.")
        break

    else:
        print("Digite uma opção válida.")

