
def area(largura,comprimento):
    area=largura*comprimento
    print(f'A área do terreno de {largura}x{comprimento} é {area} m².')

print("Vamos calcular a área de um terreno.\nInsira as informações abaixo:")
largura=float(input('LARGURA(m): '))
comprimento=float(input('COMPRIMENTO(m): '))
area(largura,comprimento)
