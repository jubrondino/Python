matriz=[[0,0,0],[0,0,0],[0,0,0]]
somatotal=soma_col3=maior=0
print('Vamos construir uma matriz.')

for l in range (0,3):
    for c in range(0,3):
        matriz[l][c]=int(input(f'Digite um valor para [{l},{c}]: '))

print('=+'*20)

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
        if matriz[l][c] % 2 == 0:
            somatotal += matriz[l][c]
    print()
print('=+'*20)

for l in range(0,3):
    soma_col3+=matriz[l][2]

for contador in range(0,3):
    if contador==0:
        maior=matriz[1][c]
    elif matriz[1][c]>maior:
        mai=matriz[1][c]
    
print(f'A soma total da matriz é {somatotal}.')
print(f'A soma da terceira coluna é {soma_col3}.')
print(f'O maior valor da segunda linha é {maior}.')