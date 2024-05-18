#exercicio 64
num = int(input('digite o numero que você quiser: '))
t = len(str(num))
s = num
print('Legal, você viu como funciona.. Para não repetirmos isso basta digitar: 999')
print('-=' *10)
while num != 999:
    num = int(input('digite outro numero inteiro: '))
    t += len(str(num))
    s += num
    if num == 999:
        print('acabou')
        s -= 999
        t -= 3
print('você digitou {} n° inteiros e a soma de todos eles foi de: {}'.format(t, s))
