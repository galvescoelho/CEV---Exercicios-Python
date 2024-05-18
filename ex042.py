#exercicio 42
from time import sleep
print('forma um triangulo? vamos descobrir!')
r1 = int(input('tamanho da 1° reta? '))
r2 = int(input('tamanho da 2° reta: '))
r3 = int(input('tamanho da 3° reta: '))
print('-------------------------------')
print('calculando....')
sleep(2)
if (r1<r2+r3) and (r2<r1+r3) and (r3<r1+r2):
    print('essas retas formam um triangulo ', end='')
    if r1 == r2 == r3:
        print('equilatero')
    elif r1 != r2 != r3 != r1:
        print('escaleno')
    elif r1 == r2 != r3 or r2 == r3 != r1 or r3 == r1 != r2:
        print('isósceles')
else:
    print('essas retas não podem formar um triangulo!')
print('-------------------------------')
print('obrigado por usar o triangulo formulator')