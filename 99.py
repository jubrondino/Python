from time import sleep

def analise(*num):
    contador=0
    print('+-'*30)
    print('Analisando os valores passados...')
    maior=0
    for numero in num:
        sleep(0.5)
        print(f'{numero}',end=' ')
        contador+=1
        if numero>maior:
            maior=numero

    print(f'\nForam informados {contador} números ao todo. ')
    print(f'O maior número foi {maior}.')

analise(1,2,3,4,5)
analise(-1,2,7,6,8,9,19)