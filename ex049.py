#exercicio 49
n = int(input('Você quer a tabuada de qual numero? '))
m = 1
for tabuada in range(1, 11):
    print('{} x {:2} = {}'.format(n, tabuada, n*tabuada))
print('------------------------------')
print('obrigado por utilizar a tabuada automatica')