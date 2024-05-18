#exercicio 60
n = int(input('qual numero você quer fatorar? '))
t = n
f = 1
while t > 1:
    f = f * t
    t -= 1
print('{}! é igual a: {}'.format(n, f))
