# exercicio 34
print('hoje é dia de aumento na bergs company')
print('vamos calcular seu aumento agora!')
salario = float(input('qual o valor do seu salario? '))
print('----------------------------------')
if salario <= 1250:
    aumento = (15/100)*salario
    print('você recebeu 15% de aumento, seu novo salario é: R$ {:.2f}'.format(aumento+salario))
else:
    aumento = (10/100)*salario
    print('você recebeu 10% de aumento, seu novo salario é: R$ {:.2f}'.format(aumento+salario))
print('obrigado pelo seu trabalho! você merece esse aumento.')