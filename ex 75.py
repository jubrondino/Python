tuplas=()

for c in range(1,5):
    numero=int(input(f"Digite o {c}º número:"))
    tuplas+=(numero,)

print(f"Você digitou os números:")
for i,c in enumerate(tuplas):
    print(f'{c}',end=',' if i < len(tuplas)-2 else ' e ' if i==len(tuplas)-2 else '.')
print(f"\nO número 9 apareceu {tuplas.count(9)} vezes")
if 3 in tuplas:
    print(f"O número 3 aparece na posição {tuplas.index(3)+1}ª posição.")
else:
    print("O valor 3 não foi digitado.")
print("Os valores pares digitados são:")
for c in tuplas:
    if c % 2==0:
        print(c, end=' ')