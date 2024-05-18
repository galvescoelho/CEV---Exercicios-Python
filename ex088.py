#exercicio 88
from random import randint
from time import sleep
l_jogo = []
l_jogadas = []
print('-'*30)
print(f'{" JOGO NA MEGA SENA ":^30}')
print('-'*30)
num = int(input('Quantos jogos você quer que eu sorteie: '))
for jogada in range(0, num):
    for jogo in range(0, 6):
        jogo = randint(1, 60)
        if jogo not in l_jogo:
            l_jogo.append(jogo)
            if len(l_jogo) == 6:
                l_jogadas.append(sorted(l_jogo[:]))
                l_jogo.clear()

print(f'-=-=-=- SORTEANDO {num} JOGOS -=-=-=-')
for p, n in enumerate(l_jogadas):
    sleep(1)
    print(f'JOGO {p+1}: {l_jogadas[p]}')
sleep(1)
print('-='*5,' BOA SORTE ','=-'*5)