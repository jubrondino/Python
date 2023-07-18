print("""

                      Você sabe o que é palíndromo?
    São palavras que de trás pra frente são iguais as palavras na sua forma normal.
                      Ex: Ana, Radar, Arara etc...
    Esse programa permite você descobrir se uma frase ou palavra é um políndromo

""")

frase_str=str(input("Digite sua frase/palavra:\n"))
frase=frase_str.replace(' ','')

if frase.lower()==frase[::-1].lower():
    print(f"'{frase_str}' é um palíndromo.")
else:
    print(f"'{frase_str}' não é um palíndromo.")