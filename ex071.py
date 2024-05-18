#exercicio 71
resto = 0
print('==============================')
print('         BANCO COELHO         ')
print('==============================')
saque = int(input('qual valor você quer sacar? '))
resto = saque
while True:
    if resto >= 50:
        notas_cin = int(resto/50)
        print(f'Total de {notas_cin} notas de R$50.')
        resto -= (notas_cin*50)
    elif 20 <= resto < 50:
        notas_vin = int(resto/20)
        print(f'Total de {notas_vin} notas de R$20.')
        resto -= (notas_vin * 20)
    elif 10 <= resto < 20:
        notas_dez = (resto/10)
        print(f'Total de {notas_cin} notas de R$10.')
        resto -= (notas_dez * 10)
    elif 1 <= resto < 10:
        print(f'Total de {resto} notas de RS1.')
        resto -= (resto)
    elif resto == 0:
        break
print('==============================')
print('VOLTE SEMPRE AOS BANCOS COELHO')