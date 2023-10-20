lista=[[],[]]

print('Insira 7 números inteiros aleatórios:')

for contador in range(0,7):
    numero=int(input(f'Digite o {contador+1}º número: '))
    if numero%2==0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)

lista[0].sort()
lista[1].sort()

print(f'Os números pares são {lista[0]}')
print(f'Os números ímpares são {lista[1]}')