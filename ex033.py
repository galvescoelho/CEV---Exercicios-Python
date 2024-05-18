#exercicio 33
print('vamos descobrir o maior dos numeros!')
n1 = int(input('digite o 1° numero: '))
n2 = int(input('digite o 2° numero: '))
n3 = int(input('digite o 3° numero: '))
# verificando quem é o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3
# verificando quem é o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3
print('--------------------------------------')
print('o maior n digitado foi: {}'.format(maior))
print('o menor n digitado foi: {}'.format(menor))

print('--------------------------------------')
print('obrigado por usar o checador de numeros!')