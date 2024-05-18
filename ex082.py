#exercicio 82
lista = []
l_impar = []
l_par = []
#adicionar numeros indefinidos na lista principal!
while True:
    num = int(input('digite um n°: '))
    lista.append(num)
    while True: #adicionar mais numeros? s ou n
        m = str(input('quer continuar?[S/N] ').upper())
        if m == 'N' or m == 'S':
            break
        else:
            print('Digite "S" para sim, "N" para não')
    print('-'*30)
    if m == 'N':
        break
#Descobrindo se o n° dentro da lista é impar ou par e adicionando em seu respectivo cenario.
for n in lista:
    if n % 2 == 0:
        l_par.append(n)
    else:
        l_impar.append(n)

print(f'os numeros digitados foram: {lista}')
print(f'os valores impares digitados foram: {l_impar}')
print(f'os valores pares digitados foram: {l_par}')