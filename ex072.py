print('impressão de numeros por extenso!')
extenso = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoite',
           'dezenove', 'vinte')
num = int(input('digite um n° entre 0 e 20: '))
while num < 0 or num > 20:
   num = int(input('digite um n° entre 0 e 20: '))
print(f'você digitou o numero {extenso[num]}')
