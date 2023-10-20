from random import randint

palpites = []
jogo = 0

print("-" * 40)
print(f"{'MEGA SENA':^40}")
print("-" * 40)

total_jogos = int(input('Você quer que eu crie quantos jogos? '))

while jogo < total_jogos:
    contador = 0
    jogo += 1
    novo_jogo = []
    while True:
        num = randint(1, 60)
        if num not in novo_jogo:
            novo_jogo.append(num)
            contador += 1
        if contador == 6:
            break
    palpites.append(novo_jogo)

for c in palpites:
    print(c)
