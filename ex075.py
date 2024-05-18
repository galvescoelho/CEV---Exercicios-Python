#exercicio 75
num = (int(input('digite um n° inteiro: \033[37m[0 a 9] \033[m')),
       int(input('digite um n° inteiro: \033[37m[0 a 9] \033[m')),
       int(input('digite um n° inteiro: \033[37m[0 a 9] \033[m')),
       int(input('digite um n° inteiro: \033[37m[0 a 9] \033[m')))
tuple = (num)
print('-----------------------------')
print(f'Voce digitou os numeros{tuple}')
# letra (A) quantas vezes o numero 9 apareceu?
print(f'O numero [ 9 ] apareceu {tuple.count(9)} vezes')
# letra (B) qual a primeira posição que foi digitado o 3 (se é que ele foi digitado..)
if 3 in tuple:
    print(f'A primeira posição em que o n° 3 apareceu foi: {tuple.index(3)+1}° posição')
else:
    print('O n° 3 não foi digitado nenhuma vez')
#descobrindo se algum numero é par
print('Os n° pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')