from random import randint
from operator import itemgetter
jogos={}
for i in range(0,4):
    numero=randint(1,6)
    print(f'O jogador {i+1} tirou {numero}.')
    jogos[f'Jogador {i+1}']=numero

ranking={}
ranking=sorted(jogos.items(),key=itemgetter(1),reverse=True)
print('\n\nRanking:\n')
for i, v in enumerate(ranking):
    print(f'{i+1}ºlugar: {v[0]} com {v[1]} pontos.')
