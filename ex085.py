#exercicio 85
lista = [[], []]
for n in range(0, 7):
    num = int(input(f'Digite o {n+1}° numero: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)

print(f'Os valores pares digitados foram: {sorted(lista[0])}')
print(f'Os valores impares digitados foram: {sorted(lista[1])}')
