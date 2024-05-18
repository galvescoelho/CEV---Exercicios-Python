#exercicio 79
lista_numeros = []
while True:
    num = int(input('digite um valor inteiro: '))
    if num in lista_numeros:
        print('esse valor não foi adicionado!')
    else:
        lista_numeros.append(num)  # adicionando 'nun' na lista_numeros na ultima posição.

        print('Este valor foi adicionado!')
    mais = str(input('quer continuar?[S/N] ').upper())
    while True:  # questionando se a pessoa deseja continuar ou não.

        if mais == 'S' or mais == 'N':
            break
        else:
            print('digite "S" para sim, "N" para não')
    print('-' * 30)
    if mais == 'N':
        break
lista_numeros.sort()
print(f'Os numeros digitados foram: {lista_numeros}')