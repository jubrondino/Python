quantidade=0
soma=0
print("Enquanto você ir digitando os números o programa irá somá-los.Para parar digite 999.")

while True:
    numero=int(input('Digite um número:'))


    if numero==999:
        break
    soma += numero
    quantidade += 1

print(f"Você digitou {quantidade} números e a soma deles foi {soma - 999}.\nComo você digitou 999, encerraremos o programa.")
