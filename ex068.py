#exercicio 68
from time import sleep
import random
print('VAMOS JOGAR PAR OU IMPAR!')
print('~' *25)
v = 0
while True:
    lista = random.randint(1, 10)
    esc = str(input('Par ou Impar?\033[37m[P / I]\033[m ').upper())
    num = int(input('Diga o valor: '))
    print('~' * 25)
    sleep(1)
    if (num+lista)%2 == 0 and esc == 'I':
        print(f'Você jogou {num} e o computador jogou {lista}, total de {num+lista} é par')
        print('Você perdeu')
        break
    elif (num+lista)%2 != 0 and esc == 'I':
        print(f'Você jogou {num} e o computador jogou {lista}, o total de {num+lista} é impar')
        print('Você ganhou')
        print('~' * 25)
        v += 1
    elif (num+lista)%2 == 0 and esc == 'P':
        print(f'Você jogou {num} e o computador jogou {lista}, o total de {num+lista} é par')
        print('você ganhou!')
        print('~' * 25)
        v += 1
    elif (num+lista)%2 != 0 and esc == 'P':
        print(f'Você jogou {num} e o computador jogou {lista}, o total de {num+lista} é impar')
        print('Você perdeu!')
        break
print('~' * 25)
print('Game Over')
if v == 1:
    print('você venceu apenas 1 vez')
elif v >= 2:
    print(f'você venceu {v} vezes! foi bem..')
elif v == 0:
    print('tu é ruim, em? não ganhou nenhuma!')