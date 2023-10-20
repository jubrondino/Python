from time import sleep

def contador(inicio,fim,passo):
    print()
    print('~'*30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
    if inicio<fim:
        for contador in range(inicio,fim+1,passo):
            print(f'{contador}',end=' ')
            sleep(0.5)

    elif inicio>fim:
        for contador in range(inicio, fim - 1, -passo):
            print(f'{contador}', end=' ')
            sleep(0.5)


contador(1,10,1)
contador(10,0,2)
print('Agora é sua vez!')

while True:
    inicio=int(input('\nDigite o ínicio da contagem: '))
    fim=int(input('\nDigite o fim da contagem: '))
    passo=int(input('\nDigite como deseja realizar a contagem: '))
    if inicio==fim or abs(fim-inicio)<passo or passo==0:
        print('\nNão é possível realizar essa contagem. Tente novamente.\n')
    else:
        contador(inicio,fim,passo)

    while True:
        opcao=input('\nDeseja continuar? (S/N):\n->').strip().upper()
        if opcao=='S':
            break
        elif opcao=='N':
            print('\n\nAté mais!\n\n\n')
            exit()
        else:
            print('\nOpção inválida. Tente novamente.\n\n')