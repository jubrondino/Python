numero_extenso = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Quatorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")

while True:
    escolha_usuario= int(input("Digite um número de 0 a 20: "))
    if escolha_usuario < 0 or escolha_usuario > 20:
        print("Escolha um número dentro do intervalo informado.")
        continue
    else:
        print(f"O número escolhido foi {numero_extenso[escolha_usuario]}.")

        while True:
            escolha_continuar = input("Deseja continuar? [S/N]: ").strip().upper()
            if escolha_continuar == 'S':
                break
            elif escolha_continuar == 'N':
                print("Até mais.")
                exit()  # Encerra o programa quando o usuário escolhe "N"
            else:
                print("Opção inválida. Tente novamente.")
