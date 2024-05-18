#exercicio 53
print('palindromo ou não? vamos descobrir')
frase = str(input('digite a frase:')).strip().lower().replace(' ','')
print('{} ao contrario é: {}'.format(frase, frase[::-1]))
if frase == frase[::-1]:
    print('a frase é um palindromo')
else:
    print('a frase não é um palindromo')