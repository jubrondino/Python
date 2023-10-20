from sys import exit

dados=[]

print('*-'*30)

while True:
    jogador={
    "nome":input('Nome do jogador:'),
    "partidas":int(input('Quantas partidas ele jogou:')),
    "gols":[] }

    for contador in range(0,jogador["partidas"]):
        jogador["gols"].append(int(input(f'Números de gols no {contador+1}º jogo: ')))

    dados.append(jogador)

    while True:
        decisao=int(input('Deseja continuar?\n1-Sim\n2-Não\n->'))
        if decisao==1 or decisao==2:
            break
        else:
            print('\nPor favor, Digite uma opção válida.\n')
    if decisao==2:
        break

for i in jogador.keys():
    print(f'{i:<15}',end=' ')
print()
for k,v in enumerate(dados):
    for d in v.values():
        print(f'{str(d):<15}',end=' ')
