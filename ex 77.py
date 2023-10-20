tuplas=('Malu','Celia','Juliana','Paulo')

for palavra in tuplas:
    print(f"\nNa palavra {palavra.upper()} temos:",end=' ')

    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')