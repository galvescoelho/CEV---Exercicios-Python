#exercicio 48
s = 0
for impar in range (1, 501):
    if impar % 2 != 0 and impar % 3 == 0:
        s += impar
print('a soma dos multiplos de 3 que são inpares até 500, é igual a: {}'.format(s))