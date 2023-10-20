
expressao=str(input("Digite uma expressão matemática:"))
pilha=[]
for caractere in expressao:
    if caractere=='(':
        pilha.append('(')
    elif caractere==')':
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(')')

if len(pilha)==0:
    print("Expressão válida.")

else:
    print("Expressão inválida.")