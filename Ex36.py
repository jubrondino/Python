

def dados():
    print("""
*********************FINANCIAMENTO IMOBILIÁRIO**********************

 Para validação do empréstimo precisaremos de algumas informações:

""")
    valor_imovel=float(input("Valor do imóvel a ser financiado: R$ "))
    salario_bruto = float(input("Salário bruto atual do comprador: R$ "))
    prazo=int(input("Prazo em anos para quitação do imóvel: "))

    print("********************************************************************")

    juros_mensais=0.006

    valor_parcela=(valor_imovel/(prazo*12))+(valor_imovel*juros_mensais) #valor do imovel com reajuste de juros mensal, dividido pelo prazo convertido em meses

    return valor_imovel,salario_bruto,prazo,valor_parcela

def inss(salario_bruto):

    if salario_bruto<=1309:
        desconto_inss=0.925

    elif salario_bruto>=1309 and salario_bruto<=2089.6:
        desconto_inss=0.91

    elif salario_bruto>=2089.61 and salario_bruto<=3134.4:
        desconto_inss=0.88

    else:
        desconto_inss=0.86

    salario_desc_inss=salario_bruto*desconto_inss

    return salario_desc_inss

def irrf(salario_desc_inss):

    if salario_desc_inss>=1903.99 and salario_desc_inss<=2826.65:
        desconto_irrf=0.925

    elif salario_desc_inss>=2826.66 and salario_desc_inss<=3751.05:
        desconto_irrf=0.85

    elif salario_desc_inss>=3751.06 and salario_desc_inss<=4664.68:
        desconto_irrf=0.775

    elif salario_desc_inss>=4664.68:
        desconto_irrf=0.725

    else:
        desconto_irrf=1

    salario_liquido=salario_desc_inss*desconto_irrf

    return salario_liquido


def emprestimo(salario_liquido,valor_parcela):

    if valor_parcela>salario_liquido*0.3:
        print(f"""
    Infelizmente não será possível realizar o empréstimo. Nas condições acima descritas o valor mensal
    da parcela é de R${valor_parcela:.2f}, o que representa mais de 30% do seu salário liquido (R${salario_liquido:.2f}), impossibilitando o empréstimo.""")

    else:
        print(f"\nParabéns! O financiamento do seu imóvel foi aprovado. O valor da parcela será de R${valor_parcela:.2f} mensais")



valor_imovel, salario_bruto, prazo, valor_parcela = dados()
salario_desc_inss=inss(salario_bruto)
salario_liquido=irrf(salario_desc_inss)
emprestimo(salario_liquido, valor_parcela)
