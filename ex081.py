#exercicio 81
lista = []
while True:
    num = (int(input('digite um valor: ')))
    lista.append(num)
    while True:
        mais = str(input('Quer continuar?[S/N] ').upper())
        if mais == 'N' or mais == 'S':
            break
        else:
            print('Digite "S" para sim, "N" para não.')
    print('-'*30)
    if mais == 'N':
        break
# A) quantos numeros foram digitados:
print(f'{len(lista)} n° foram digitados.')

# B) lista dos valores em ordem decrescente:
print(f'a lista de forma decrescente dos valores será: {sorted(lista, reverse=True)}')

# C) o valor 5 foi digitado? se sim, qual a posição dele na lista(se estiver)
if 5 in lista:
    print(f'o valor 5 foi digitado, está na posição {lista.index(5)+1}')
else:
    print('o valor 5 não foi digitado nenhuma vez.')