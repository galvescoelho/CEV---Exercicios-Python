#exercicio 45
import random
from time import sleep
print('vamos jogar jokenpo? \033[34mVocê\033[m x \033[35mComputador!\033[m')
print('\033[34mQuem vai ganhar esse duelo?\033[m')
print('-=-' *13)
lista = ['pedra', 'papel', 'tesoura']
jogada_pc = random.choice(lista)
jogada_us = int(input('''P/ Pedra \033[34m digite [ 1 ]\033[m
P/ Papel \033[34m digite [ 2 ]\033[m
P/ Tesoura \033[34m digite [ 3 ]\033[m
Escolha sua jogada: '''))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-=-' *13)
if jogada_us == 1 and jogada_pc == 'papel':
    print('''Jogada do Pc: \033[35mPapel\033[m
Sua jogada : \033[34mPedra\033[m
Papel ganha de Pedra! \033[31mVocê perdeu\033[m''')
elif jogada_us == 1 and jogada_pc == 'tesoura':
    print('''Jogada do Pc: \033[35mTesoura\033[m
Sua jogada : \033[34mPedra\033[m
Pedra ganha de tesoura!! \033[32mVocê ganhou!\033[m''')
elif jogada_us == 1 and jogada_pc == 'pedra':
    print('''Jogada do Pc: \033[35mPedra\033[m
Sua jogada : \033[34mPedra\033[m
Pedra empata com pedra. \033[97mNinguem ganhou!\033[m''')
elif jogada_us == 2 and jogada_pc == 'pedra':
    print('''Jogada do Pc: \033[35mPedra\033[m
Sua jogada : \033[34mPapel\033[m
Papel ganha de Pedra! \033[31mVocê ganhou\033[m''')
elif jogada_us == 2 and jogada_pc == 'tesoura':
    print('''Jogada do Pc: \033[35mTesoura\033[m
Sua jogada : \033[34mPapel\033[m
Tesoura corta o papel!! \033[32mVocê perdeu!\033[m''')
elif jogada_us == 2 and jogada_pc == 'papel':
    print('''Jogada do Pc: \033[35mPapel\033[m
Sua jogada : \033[34mPapel\033[m
Papel embrulha papel?. \033[97mNinguem ganhou!\033[m''')
elif jogada_us == 3 and jogada_pc == 'pedra':
    print('''Jogada do Pc: \033[35mPedra\033[m
Sua jogada : \033[34mTesoura\033[m
Pedra quebra a tesoura! \033[31mVocê perdeu.\033[m''')
elif jogada_us == 3 and jogada_pc == 'tesoura':
    print('''Jogada do Pc: \033[35mTesoura\033[m 
Sua jogada : \033[34mTesoura\033[m
Tesoura corta tesoura? \033[97mNinguem ganhou!\033[m''')
elif jogada_us == 3 and jogada_pc == 'papel':
    print('''Jogada do Pc: \033[35mPapel\033[m
Sua jogada : \033[34mTesoura\033[m
Tesoura corta papel!. \033[32mvocê ganhou!\033[m''')
else:
    print('\033[31mInsira uma opção válida para jogar!\033[m')