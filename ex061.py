#exercicio 61
começo = int(input('quer começar em qual numero? '))
salto = int(input('contar de quanto em quanto? '))
x = 0
while x < 10:
    print(começo)
    começo += salto
    x += 1
print('acabou')