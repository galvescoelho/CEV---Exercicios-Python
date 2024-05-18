#exercicio 62
começo = int(input('quer começar em qual numero? '))
salto = int(input('contar de quanto em quanto? '))
print('----------------')
x = 10
contagem = 0
while x != 0:
    print(começo, end=' → ')
    começo += salto
    x -= 1
    contagem += 1
    if x == 0:
        print('pausa')
        x = int(input('você quer mais quantos termos? '))
        print('---------------------')
print('neste teste, utilizamos {} termos'.format(contagem))
print('acabou')