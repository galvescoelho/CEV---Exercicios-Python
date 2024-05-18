#exercicio 86
lista = [[], [], []]
cont = 0
for c in range(0,9):
    num = int(input('digite um numero: '))
    cont += 1

    #condicionando em qual lista cada n° será adicionado.
    if cont <= 3:
        lista[0].append(num)
    elif cont <=6:
        lista[1].append(num)
    else:
        lista[2].append(num)
print('-'*30)
#subdividir as listas em lista
for sub_lista in lista:
    for n in sub_lista:
        print(f'[{n:^5}]', end='')
    print() #para quebra de linha