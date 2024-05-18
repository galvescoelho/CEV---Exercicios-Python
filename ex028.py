#exercicio 28
import random
from time import sleep
num = random.randint(1, 5)
print('estou pensando em um numero entre 1 e 5..')
n = int(input('em que numero estou pensando? '))
if n == num:
    print('processando resposta..')
    sleep(2)
    print('eu estava pensando em {}! você acertou!'.format(num))
else:
    print('processando resposta..')
    sleep(2)
    print('você não acertou.. eu estava pensando em {} e não em {}'. format(num, n))


