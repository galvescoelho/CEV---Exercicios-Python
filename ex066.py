print('vamos jogar valores ao vento..')
print('você vai digitar quantas x quiser, e o codigo de parada é [999]')
num = int(input('digite um numero: '))
s = num
cont = 1
while True:
    num = int(input('digite mais um numero: '))
    if num == 999:
        break
    s += num
    cont += 1
print(f'a soma dos {cont} valores é igual a {s}')
