#exercicio 36
#emprestimo
from time import sleep
print('\033[33mEmprestimo banco inter\033[m')
print('Vamos conferir se você tem financiamento aprovado!')
print('\033[33m-=-\033[m' *15)
nome = str(input('olá, como você se chama? '))
sal = float(input('qual o valor do seu salario, \033[33m{}\033[m? '.format(nome.title())))
imov = float(input('qual o valor do \033[33mimovel\033[m que você esta de olho? '))
tempo = float(input('você quer pagar esse \033[33mimovel\033[m em quantos anos? '))
print('\033[33m-=-' *15)
print('calculando.. aguarde um instante\033[m')
preço_anual = (imov/tempo)
sal_anual = (sal*12)
aceitavel = (30/100)*sal_anual
if aceitavel >= preço_anual:
    sleep(2)
    print('parabéns! o seu \033[33memprestimo imobiliario\033[m foi aprovado!')
    print('você conseguirá pagar as parcelas mensais de {:.3f} referente ao valor do seu imovel {:.3f}'.format(preço_anual/12, imov))
else:
    sleep(2)
    print('\033[31mInfelizmente seu emprestimo foi negado, o valor da parcela: R$ {:.3f} é superior a 30% do seu salario!\033[m'.format(preço_anual/12))
    print('você precisa procurar imoveis que tenham parcelas mensais de até {} para que você consiga pagar!'.format(aceitavel/12))
print('\033[33mobrigado por simular o financiamento do seu imovel conosco!')

