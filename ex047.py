#exercicio 47
print('contagem dos pares.. vamosm lá!')
f = int(input('voce quer que eu conte até quanto? '))
f = f+1
for contagem in range (0, f):
    if contagem%2 == 0:
        print(contagem)