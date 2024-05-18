#exercicio 44
from time import sleep
print('\033[34mAPP PagFacil! aproveite os descontos de maio.\033[m')
usuario = str(input('Seja bem vindo, usuario(a)! como você se chama? ').title())
compra = int(input('Qual foi o valor da sua compra, {}? '.format(usuario)))
pagamento = int(input('''    - OPÇÕES DE PAGAMENTO -
-----------------------------------
P/ PAGAMENTO À VISTA (10% DE DESCONTO) \033[37m digite [ 1 ]\033[m
P/ PAGAMENTO À VISTA NO CARTÃO (5% DE DESCONTO) \033[37m digite [ 2 ]\033[m
P/ PAGAMENTO EM 2X NO CARTÃO (SEM JUROS) \033[37m digite [ 3 ]\033[m
P/ PAGAMENTO EM 3X OU MAIS NO CARTÃO (20% DE JUROS) \033[37m digite [ 4 ]\033[m\n'''))
print('----------------------------')
print('\033[34mProcessando pagamento.. Aguarde um pouco..\033[m')
sleep(2)
if pagamento == 1:
    print('Ótimo {}, você escolheu pagamento à vista, o valor da sua compra ficará no total de: R$ {:.2f}.'.format(usuario, compra*0.9))
elif pagamento == 2:
    print('Certo {}, você escolheu pagar à vista no cartão, o valor com desconto será: R$ {:.2f}'.format(usuario, compra*0.95))
elif pagamento == 3:
    print('Você escolheu pagar em 2X no cartão, como não tem desconto, você irá pagar o valor total! R$ {:.2f}'.format(usuario, compra))
elif pagamento == 4:
    print('Iremos dividir sua compra em 3X, {}. Com o juros ficará um total de: R$ {:.2f}'.format(usuario, compra*1.20))
else:
    print('Opção invalida! Insira uma opção valida.')