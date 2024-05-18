#exercicio 54
from datetime import date
ano_atual = date.today().year #puxando o ano atual para calcular idade das pessoas
print('serviço de maior idade registrator ibge')
print('-------------------------------')
smaior = 0
smenor = 0
pessoa = 1
for pessoas in range (0, 7):
    ano_nascimento = int(input('em qual ano o {}° nasceu? '.format(pessoa)))
    idade = ano_atual - ano_nascimento
    pessoa += 1
    if idade >= 18:
        smaior += 1
    elif 0 < idade < 18:
        smenor += 1
    elif idade < 0:
        print('essa pessoa ainda nem nasceu, conta outra..')
print('-------------------------------')
print('nessa casa temos {} pessoas maiores de idade..'.format(smaior))
print('enquanto temos {} de menor!'.format(smenor))