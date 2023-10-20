pessoa = {}
lista=[]
soma = 0
mulheres=[]
contador=0

while True:
    contador+=1
    print(f'Dados da {contador}ª pessoa:')
    pessoa['nome'] = input('Nome:')
    while True:
        pessoa['sexo'] = input('Sexo[M/F]:').strip().upper()
        if pessoa['sexo']=='F' or pessoa['sexo']=='M':
            break;
        else:
            print('\nVocê precisa digitar F ou M.\n')
    pessoa['idade'] = int(input('Idade:'))
    soma += pessoa['idade']
    lista.append(pessoa.copy())
    pessoa.clear()
    while True:
        opcao=str(input('Deseja continua? [S/N]:\n->')).strip().upper()
        if opcao=='N' or opcao=='S':
            break;
        else:
            print('\nDigite uma opção válida.\n')
    if opcao=='N':
        break;

media = soma / contador



print(f'A média das idades cadastradas é {media:.2f}')
print(f'{contador} pessoas foram cadastradas')
print('As pessoas do sexo feminino cadastradas são:',end='')
for pessoa in lista:
    if pessoa['sexo']=='F':
        print(pessoa['nome'],end=' ')
print('\nAs pessoas com idade maior que a média de idade são:\n',end='')
for pessoa in lista:
    if pessoa['idade']>=media:
        for i,k in pessoa.items():
            print(f'{i}={k}',end=',')