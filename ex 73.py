times=("Flamengo", "Internacional", "Atlético Mineiro", "São Paulo", "Fluminense", "Grêmio", "Palmeiras", "Santos", "Athletico Paranaense", "Bragantino", "Ceará", "Corinthians", "Atlético Goianiense", "Bahia", "Sport Recife", "Fortaleza", "Vasco da Gama", "Goiás", "Coritiba", "Botafogo")

print("Os 5 primeiros colocados são:")
for c in range(0,5):
    print(f"{c+1} - {times[c]}")
print()
print("Os 4 últimos colocados são:")
for c in range(16,20):
    print(times[c])
print()

times_ordenados=sorted(list(times))
print("Os  times em ordem alfabética são:")

for c in times_ordenados:
    print(c)

print(f"O São Paulo está na {times.index('São Paulo')+1}ª posição")
