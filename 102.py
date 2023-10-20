
def fatorial(numero,show=False):
    """

    :param numero: o numero a ser calculado
    :param show:(opcional) Mostra ou não a conta
    :return:0
    """
    fat = 1
    for num in range(1,numero+1):
        fat*=num
        if show:
            if num<numero:
                print(f'{num}*',end='')
            else:
                print(f'{num}=',end='')

    print(fat)

fatorial(3,True)
help(fatorial)