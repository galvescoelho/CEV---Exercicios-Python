#exercicio 38
print('vamos verificar qual é maior!')
n1 = int(input('Digite o 1° N°: '))
n2 = int(input('Digite o 2° N°: '))
if n1 > n2:
    print('O primeiro valor [{}] é o maior!'.format(n1))
elif n2 > n1:
    print('O segundo valor [{}] é o maior!'.format(n2))
else:
    print('Não existe valor maior! Os dois valores são iguais.')