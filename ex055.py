#exercicio 55
print('vamos descobrir quem pesa mais e quem pesa menos.. vamos começar!')
print('precisamos saber o peso de todos os 5 dessa casa!')
morador = 1
leve = 0
pesado = 0
for moradores in range(0, 5):
    peso = int(input('quanto o morador {} pesa? '.format(morador)))
    morador += 1
    if moradores == 0:
        pesado = peso
        leve = peso
    else:
        if peso > pesado:
            pesado = peso
        elif peso < leve:
            leve = peso
print('peso mais leve: {}'.format(leve))
print('mais pesado: {}'.format(pesado))