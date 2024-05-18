# exericio 35
print('forma um triangulo? vamos descobrir!')
r1 = int(input('tamanho da 1° reta? '))
r2 = int(input('tamanho da 2° reta: '))
r3 = int(input('tamanho da 3° reta: '))
if (r1>r2+r3) or (r2>r1+r3) or (r3>r1+r2):
    print('-------------------------------')
    print('calculando....')
    print('essas retas não podem formar um triangulo!')
else:
    print('-------------------------------')
    print('calculando....')
    print('essas retas podem formar um triangulo!')
print('obrigado por usar o triangulo formulator')