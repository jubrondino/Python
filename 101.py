

def voto(ano):
    from datetime import datetime
    ano_atual = datetime.today().year
    idade = ano_atual - ano
    if idade>=18 and idade<65:
        opcao="Obrigatório"
    elif idade>=16 and idade<18 or idade>65:
        opcao="Opcional"
    else:
        opcao="Negado"
    print(f'Com {idade} anos:',end='')
    return opcao


ano=int(input('Qual o ano do seu nascimento?\n->'))
opcao=voto(ano)
print(f'voto {opcao}.')

