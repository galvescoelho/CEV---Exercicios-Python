#exercicio 51
começo = int(input('você quer que comece a contar a partir de quanto? '))
salto = int(input('de quanto em quanto? '))
pa = começo + (10) * salto #formula do pa
for pa2 in range (começo, pa, salto):
    print('{}'.format(pa2))
print('fim')