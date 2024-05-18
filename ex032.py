#exercicio 32
from datetime import date
print('este ano é bissexto? vamos descobrir!!!')
ano = int(input('que ano você quer conferir? coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano {} é bissexto meu parceiro!'.format(ano))
else:
    print('esse ano ai não é não.. tente outro..')
print('-----------------------------------')
print('obrigado por usar o ano bissexto calculator!')