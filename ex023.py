#exercicio 23
n1 = str(input('escreva um numero com 4 digitos: '))
print('o numero digitado foi: \033[32m{}\033[m'.format(n1))
print('unidade: \033[32m{}\033[m'.format(n1[3]))
print('dezena: \033[32m{}\033[m'.format(n1[2]))
print('centena: \033[32m{}\033[m'.format(n1[1]))
print('milhar: \033[32m{}'.format(n1[0]))