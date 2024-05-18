#exercicio 29
print('\nmultador automatico do detran')
print('-----------------------------')
velocidade = int(input('qual era a velocidade que você estava? '))
valor_multa = (velocidade-80)*7
if velocidade <= 80:
    print('\033[32mseguindo, seguindo! ta liberado.')
else:
    print('\033[31mvocê foi multado, meliante! o valor da multa será de {} R$!'.format(valor_multa))
print('-----------------------------')
print('\033[mobrigado por usar o app multador do Detran')