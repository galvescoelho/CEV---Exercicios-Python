#exercicio 39
from datetime import date
ano_atual = date.today().year
print('\033[32mserviço de alistamento obrigatorio online.\033[m')
print('Vamos descobrir se está na hora do seu alistamento!')
print('\033[32m-=-\033[m' * 15)
idade = int(input('Em que ano você nasceu? '))
if (ano_atual-idade) <= 17:
    print('Sai daqui, seu bisonho! Ainda faltam {} anos pra você se alistar!'.format(18-(ano_atual-idade)))
elif (ano_atual-idade) == 18:
    print('Soldado ligado, veio na hora certa pra se alistar! pode pegar a enchada.')
else:
    print('Já passou da hora, soldado! Você devia ter se alistado {} anos atrás!'.format(ano_atual-(idade+18)))
    print('Passe pra dentro, bora bora! ligeiro seu caba.')
print('\033[32m-=-\033[m' * 15)
print('Obrigado por usar o serviço de alistamento online!')