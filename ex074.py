#exercicio 74
from random import randint
list = (randint(1, 10), randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20))
organizado = sorted(list)
print('Os valores sorteados foram:', end=' ')
for n in organizado:
    print(f'{n}', end=' ')
print(f'\no menor numero = {organizado[0]}')
print(f'o maior numero = {organizado[-1]}')