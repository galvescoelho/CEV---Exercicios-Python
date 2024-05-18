#exercicio 77
tupla = ('parapente', 'crocodilo', 'defusar', 'helicoptero', 'jato', 'carro')
vogais = 'aeiouAEIOU'
for palavra in tupla:
    vogais_na_palavra = ''
    print(f'\nNa palavra {palavra.upper()} temos as vogais:', end=' ')
    for letras in palavra:
        if letras.lower() in vogais:
            print(letras, end= ' ')
