#exericio 37
num = int(input('Digite um numero inteiro: '))
print('''escolha uma das bases para conversão:
[ 1 ] para Binario.
[ 2 ] para Octal.
[ 3 ] para hexadecimal.''')
escolha = int(input('sua opção: '))
if escolha == 1:
    print('{} convertido para Binario é igual a: {}!'.format(num, bin(num)[2:]))
elif escolha == 2:
    print('{} convertido para Octal é igual a: {}!'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('{} convertido para Hexadecimal é igual a: {}!'.format(num, hex(num)))
else:
    print('Opção invalida! Escolha novamente.')