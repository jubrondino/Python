from random import randint


def sorteio(inicio,fim):
    numeros = []
    for num in range(5):
        numero=randint(inicio,fim+1)
        numeros.append(numero)
    print(numeros)
    return numeros

def soma(lista):
    add=0
    for numero in lista:
        if numero%2==0:
            add+=numero
    print(f'A soma dos números pares é {add}.')

numeros_sorteados=sorteio(1,20)
soma(numeros_sorteados)

 