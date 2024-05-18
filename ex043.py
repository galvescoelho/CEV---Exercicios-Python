#exercicio 43
print('calculadora de imc!')
print('-------------------')
usuario = str(input('olá usuario(a), como você se chama? ').title())
altura = float(input('qual a sua altura, {}? \033[37m(ex: 1.70)\033[m '.format(usuario)))
peso = float(input('certo, e quanto você esta pesando? '))
imc = peso/(altura**2)
if imc <= 18.4:
    print('seu imc é {:.2f}, você está abaixo do peso!'.format(imc))
elif imc >= 18.5 and imc <= 24.9:
    print('seu imc é {:.2f}, você está no peso ideal!'.format(imc))
elif imc >= 25 and imc <= 30:
    print('seu imc é {:.2f}, você está com sobrepeso!'.format(imc))
elif imc >= 30.1 and imc <= 40:
    print('seu imc é {:.2f}, você está com obesidade!'.format(imc))
else:
    print('seu imc é {:.2f}, você está com obesidade mórbida!'.format(imc))
print('------------------------------------')
print('Obrigado por usar o nosso aplicativo para calcular imc!')