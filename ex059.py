#exercicio 59
print('calculadora digital')
opção = ''
n1 = int(input('digite o 1° numero: '))
n2 = int(input('digite o 2° numero: '))
while opção != 5:
    print('--------------------------')
    print('''MENU:
[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NUMEROS
[ 5 ] SAIR DO PROGRAMA''')
    opção = int(input('digite sua opção: '))
    if opção == 1:
        print('{} + {} = {}'.format(n1,n2, n1+n2))
    elif opção == 2:
        print('{} x {} = {}'.format(n1, n2, n1*n2))
    elif opção == 3:
        if n1 > n2:
            print('{} é maior do que {}'.format(n1, n2))
        elif n2 > n1:
            print('{} é maior do que {}'.format(n2, n1))
        elif n2 == n1:
            print('os dois valores são iguais!')
    elif opção == 4:
        n1 = int(input('digite o novo 1° numero: '))
        n2 = int(input('digite o novo 2° numero: '))
print('--------------------------------------')
print('obrigado por usar nossa calculadora moderna!')

