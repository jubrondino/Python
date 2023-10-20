alunos=[]

while True:
    aluno=[]
    nome=str(input('Nome do aluno: '))

    nota1_str=input('1º nota: ')
    nota1_str=nota1_str.replace(',','.')
    nota1=float(nota1_str)

    nota2_str=input('2º nota: ')
    nota2_str=nota2_str.replace(',','.')
    nota2=float(nota2_str)

    media=(nota1+nota2)/2

    alunos.append([nome,nota1,nota2,media])

    escolha=str(input('Deseja incluir mais algum aluno? [S/N]:')).strip().lower()
    if escolha=='n':
        break;
print('\n')
print('-'*40)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>20}')
print('-'*40)

for c, aluno in enumerate(alunos):
    print(f'{c+1:<4}{aluno[0]:<20}{aluno[3]:>10}')

while True:
    opcao=int(input('Digite o número do aluno que deseja saber a nota ou 999 para encerrar: '))-1
    if opcao==998:
        print('Finalizando.')
        break;
    if opcao<len(alunos):
        print(f'Notas de {alunos[opcao][0]} são {alunos[opcao][1]} e {alunos[opcao][2]}')