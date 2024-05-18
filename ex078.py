#exercicio 78
lista_num = []
mai = 0
men = 0
for _ in range(0, 5):
    num = int(input('digite um numero: '))
    lista_num.append(num)
    if _ == 0:
        mai = num
        men = num
    else:
        if num > mai:
            mai = num
        elif num < men:
            men = num

print('-'*30)
print(f'os numeros que você digitou foram: {lista_num}')
print(f'o maior valor digitado foi {mai}, na posição {lista_num.index(mai)+1}')
print(f'o menor valor digitado foi {men}, na posição {lista_num.index(men)+1}')
