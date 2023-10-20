listagem=('Pão', 1,'Leite', 4,'Requeijão',6,'Coca-cola',9)

print(F"""
{'-'*40}
          LISTAGEM DE PREÇOS
{'-'*40}
""")
for index in range(0,len(listagem)):
    if index%2==0:
        print(f"{listagem[index]:.<30}",end='')
    else:
        print(f"R$ {listagem[index]:.2f}")
print()
print(f"{'-'*40}")