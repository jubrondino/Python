def ficha(jogador='<desconhecido>',gols=0):
    print(f'\nO jogador {jogador} fez {gols} gol(s) no campeonato')


jog=str(input('\nNome do jogador:'))
gols=str(input('\nNº de gols:'))

if gols.isnumeric():
    gols=int(gols)
else:
    gols=0

if jog.strip()=='':
    ficha(gols=gols)
else:
    ficha(jog,gols)

