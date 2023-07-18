resultado=1

numero=int(input("Digite um número:  "))
contador = numero
while True:
    opcao= int(input("""
                MENU 
            [1] Fatorial com For
            [2] Fatorial com While
    
    """))
    print(f"{numero}!=",end='')

    if opcao==1:
        for fatorial in range(1,numero+1):
            resultado*=fatorial
            print(f"{fatorial}",end='')
            if fatorial<numero:
                print("x",end='')
        print(f"={resultado}.")

    if opcao==2:
        while contador>0:
            print(f"{contador}",end='')
            print("x" if contador>1 else "=",end='')
            resultado*=contador
            contador-=1
    print(f"{resultado}.")
