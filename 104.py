def leiaint(msg):
    while True:
        numero=str(input(msg))
        if not numero.isnumeric():
            print('\033[0;31m\nERRO!Digite um número válido.\033[m')
        else:
            valor=int(numero)
            break

    return valor


numero=leiaint('\nDigite um número: ')
print(f'\nVoce digitou o numero {numero}.')