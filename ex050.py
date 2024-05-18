#exercicio 50
s = 0
for pares in range (1, 7):
    num = int(input('digite um num inteiro: '))
    if num %2 == 0:
        s += num
print(f'a soma dos numeros pares digitados é de: {s}')