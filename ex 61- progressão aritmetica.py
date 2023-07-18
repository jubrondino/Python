
numero = int(input("Digite um número: "))
razao = int(input("Digite a razão da progressão aritmética: "))
termos = 10

while True:
    contador = 0
    while contador < termos:
        print(f"{numero}", end='')
        print("," if contador < termos - 1 else ".", end='')
        numero += razao
        contador += 1

    mais = int(input("\nQuantos termos mais deseja ver? (Digite 0 para sair) "))
    if mais == 0:
        break
    termos += mais

