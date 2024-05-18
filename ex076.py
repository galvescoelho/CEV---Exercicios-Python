#exercicio 75
tabela = (['Pão', 'Frango', 'Iogurte', 'Pizza', 'Vinho', 'Picanha'], [5.0, 13.5, 8.90, 25.0, 45.0, 59.0])
print('-' *30)
print(f'{"SACOLÃO SÃO JORGE":^30}')
print('-' *30)
for i in range(len(tabela[0])):
    print(f'{tabela[0][i]}'.ljust(25,'.')+'R$'+f'{tabela[1][i]}'.rjust(5, ' '))
print('-' *30)