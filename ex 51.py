inicio=int(input("Digite o termo que deseja iniciar a progressão aritmética:"))
fim=inicio+10
progressao=int(input("Digite a progressão:"))

for numero in range (inicio,fim+1,progressao):
    print(f"{numero}")