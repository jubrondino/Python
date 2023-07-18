#soma entre todos os multiplos de 3 e que se encontram no intervalo de 1 a 500
soma=0
for numeros in range(3,501,3):
    soma+=numeros

print(f"A soma de todos os múltiplos de 3 entre 1 e 500 é {soma}")
