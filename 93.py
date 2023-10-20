
dados={}
gols=[]
dados['nome']=str(input('Nome do jogador:'))
partidas=int(input('Quantas partidas ele jogou:'))

for contador in range(0,partidas):
    gols.append(int(input(f'Números de gols no {contador+1}º jogo: ')))

dados['gols']=gols[:]
dados['total']=sum(gols)
print('*-'*30)
print(dados)
print('*-'*30)
print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')

for contador in range(partidas):
    print(f'No {contador + 1}º jogo ele marcou {dados["gols"][contador]} gols.')

print(f'Total de gols foi {dados["total"]}.')