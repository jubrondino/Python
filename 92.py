from datetime import datetime

dados={}

print('Vamos precisar de algumas informações:')
dados['nome'] = str(input('Nome completo:'))
ano_nascimento=int(input('Ano de nascimento:'))
idade=datetime.now().year-ano_nascimento
dados['idade'] = idade
dados['carteira de trabalho'] = int(input('Número da carteira de trabalho(Caso não tenha, digite 0):'))


if dados['carteira de trabalho']!=0:
    dados['ano de contratacao'] =int(input('Ano de contratação:'))
    dados['salario'] = float(input('Salário:'))
    dados['aposentadoria']=(dados['ano de contratacao']+35)-ano_nascimento

for i,dado in dados.items():
    print(f'{i} tem o valor {dado}.')
