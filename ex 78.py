lista=[]

for c in range(1,6):
    numero=int(input(f"Digite o {c}º número:"))
    lista+=[numero,]
print(f"O maior número é {max(lista)} e está na(s) posição(ões):",end=' ')

for index, c in enumerate(lista):
    if c==max(lista):
        print(index+1,end=' ')
print(f"\nO menor número digitado foi {min(lista)} e está na(s) posição(ões): ",end='')
for index, c in enumerate(lista):
    if c== min(lista):
        print(index+1,end=' ')