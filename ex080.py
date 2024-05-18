#exercicio 80
valores = []
mai = med = men = 0
for n in range(0, 5):
    num = int(input('Digite um valor: '))
    if len(valores) == 0:
        valores.append(num)
        print('Foi adicionado ao final da lista')
        mai = med = men = num
    else:
        if num < men:
            men = num
            valores.insert(0, num)
            print('foi adicionado na posição 0')
        elif num > mai:
            mai = num
            valores.append(num)
            print('Foi adicionado ao final da lista')
        elif men < num < mai:
            med = num
            valores.insert(1, num)
            print('foi adicionado na posição 1')
        elif valores[1] < num < valores[-1]:
            valores.insert(2, num)
            print('foi adiciconado na posição 2')
        elif valores[1] < num < valores[2]:
            valores.insert(2, num)
            print('foi adiciconado na posição 2')
print(f'os valores adicionados em ordem: {valores}')