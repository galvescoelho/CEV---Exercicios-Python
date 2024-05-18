#exercicio 87
lista = [[], [], []]
cont = 0
pares = impares = som = 0
for c in range(0,9):
    num = int(input('digite um numero: '))
    cont += 1
    if cont <= 3:
        lista[0].append(num)
    elif cont <=6:
        lista[1].append(num)
    else:
        lista[2].append(num)
print('-'*30)
for sub_lista in lista:
    for n in sub_lista:
        print(f'[   {n}   ]', end='')
    print() #para quebra de linha

# A) soma de todos os valores pares digitados:
for sub_lista in lista:     #acessando as listas menores
    for n in sub_lista:
        if n %2 == 0:       #se o n° dentro da sublista divido por 2 tiver resto = 0: ele é par!
            pares += n      #somando os valores pares
print(f'os valores pares somados são igual a: {pares}')

# B) soma dos valores da 3° coluna:
for sub_lista in lista:
    if len(sub_lista) >= 3:     #verificar se a sub_lista tem ao menos 3 colunas:
        som += sub_lista[2]     #somando o item da 3° coluna ao bolo:
print(f'a soma dos valores da 3° coluna é: {som}')

# c) conferir o maior valor da segunda linha
if len(lista) >= 2:     #conferindo se a lista tem mais de 1 linha.
    print(f'O maior n°digitado na 2° linha é: {max(lista[1])}')