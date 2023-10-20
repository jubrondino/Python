from random import randint

valores=(randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print(f"Os números sorteados que compõe a tupla são:",end='')

for i, c in enumerate(valores):
    print(c,end=',' if i<len(valores)-2 else ' e ' if i==len(valores)-2 else '.')

print(f"\nO maior valor sorteado é {max(valores)}.")
print(f"O menor valor sorteado é {min(valores)}.")

