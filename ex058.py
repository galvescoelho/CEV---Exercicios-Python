#exercicio 58
import random
num = random.randint(1, 10)
chu = 1
print('vamos jogar um jogo!')
print('oi usuario, eu vou pensar em um numero entre 1 e 10')
print('esse jogo só acaba quando você acertar o numero que estou pensando! hahahaha')
print('--------------------------------------')
print('valendo!!!')
chute = int(input('{}° tentativa: '.format(chu)))
while chute != num:
    if chu <= 3:
        print('ainda não acertou! tenta dnovo!')
        chu += 1
        chute = int(input('{}° tentativa: '.format(chu)))
    elif chu >= 4:
        print('cara, vai tentar dnovo? acho que já ta bom de parar.. você quem sabe!')
        chu += 1
        chute = int(input('{}° tentativa: '.format(chu)))
print('você acertou, parabéns pequeno gafanhoto!')