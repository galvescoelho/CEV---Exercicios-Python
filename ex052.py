#exercicio 52
num = int(input('digite um numero: '))
tot = 0
for primo in range(1, num + 1):
    if num%primo == 0:
        print('\033[34m', end='→ ')
        tot += 1
    elif num%primo != 0:
        print('\033[33m', end='→ ')
    print('{} '.format(primo), end='')
if tot == 2:
    print('\n\033[m{} é primo!'.format(num))
else:
    print('\n\033[m{} não é primo!'.format(num))