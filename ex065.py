#exercicio 65
#lá vamos nós, o guanabara ta me fazendo criar cabelos brancos
num = int(input('digite um numero inteiro:'))
print('para parar de adcionar numeros, digite [ 0 ]')
tot = num
s = 1
menor = num
maior = num
while num != 0:
    num = int(input('digite outro numero:'))
    tot += num
    s += 1
    if num > maior:
        maior = num
    elif num < menor and num != 0:
        menor = num
    elif num == 0:
        tot = tot
        s = s - 1
print('acabou')
print('a soma de todos os numeros foi igual a: {} e a media deles {}'.format(tot, tot/s))
print('o menor n° foi {} e o maior n° foi: {}'.format(menor, maior))

