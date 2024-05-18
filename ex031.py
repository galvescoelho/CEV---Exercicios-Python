#exercicio 31
print('trem bala da colina calculator')
print('-----------------------------')
km = int(input('quantos km você ira viajar? '))
if km <= 200:
    valor_km = 0.5*km
    print('sua viagem de {} km, custará: {} R$'.format(km, valor_km))
else:
    valor_km = 0.45*km
    print('sua viagem de {} km, custará: {} R$'.format(km, valor_km))
print('-----------------------------')
print('obrigado por viajar conosco mais uma vez!')