#exercicio 41
from datetime import date
ano_atual = date.today().year
print('Inscrição digital para comissão esportiva brasileira.')
atleta = str(input('Olá atleta, como você se chama? ').title())
ano_nascimento = int(input('Em qual ano você nasceu, {}? '.format(atleta)))
idade = ano_atual-ano_nascimento
if idade <= 9:
    print('{}, acabamos de realizar sua inscrição na categoria: \033[32mMirim.\033[m'.format(atleta))
elif idade >= 10 and idade <= 14:
    print('{}, acabamos de realizar sua inscrição na categoria: \033[32mInfantil\033[m'.format(atleta))
elif idade >= 15 and idade <= 19:
    print('{}, acabamos de realizar sua inscrição na categoria: \033[32mJunior\033[m'.format(atleta))
elif idade == 20:
    print('{}, acabamos de realizar sua inscrição na categoria: \033[32mSênior\033[m'.format(atleta))
else:
    print('{}, acabamos de realizar sua inscrição na categoria: \033[32mMaster\033[m'.format(atleta))
print('\033[32mSeja muito bem vindo ao time Brasil!\033[m')