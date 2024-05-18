#exercicio 73
serie_a = ('ahtletico paranaense', 'bahia', 'botafogo', 'atletico mineiro',
           'bragantino', 'palmeiras', 'flamengo', 'são paulo', 'internacional',
           'cruzeiro', 'gremio', 'fortaleza', 'cricíuma', 'corinthians', 'juventude',
           'fluminense', 'vasco da gama', 'vitoria', 'atletico - GO', 'cuiabá')
print('=-' *20)
print(f'Os 5 primeiros colocados do brasileirão são: {serie_a[:5]}')
print('=-' *20)
print(f'Os ultimos 4 colocados do brasileirão são: {serie_a[16:]}')
print('=-' *20)
print(f'Os times da serie A em ordem alfabetica: {sorted(serie_a)}')
print('=-' *20)
print(f'O vasco está na {serie_a.index('vasco da gama')+1}° posição')
