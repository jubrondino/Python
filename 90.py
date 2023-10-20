'''Faça um programa que leia nome e média de um alno,4guardando também a situaão em um dicionário.
 No final mostre o conteudo da estrutura na tela.'''


aluno={}

print('Preencha com os dados do aluno:')
aluno['nome']=str(input('Nome: '))
aluno['media']=float(input('Média: '))
aluno['situacao']=str(input('Situação(Aprovado/Reprovado): '))


print(f'O aluno(a) {aluno["nome"]} com média {aluno["media"]} está {aluno["situacao"]}.')