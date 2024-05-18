#exercicio 84
group = list()
pessoa = list()
maisl = maisp = 0
while True:
    pessoa.append(str(input('Como se chama? ')))
    pessoa.append(int(input('Quanto pesa? ')))
    group.append(pessoa[:])
    pessoa.clear()
    while True:
        cont = str(input('Quer adicionar + alguem?[S/N] ').upper())
        if cont == 'S' or cont == 'N':
            break
        else:
            print('Digite "S" para sim, "N" para não')
    print('-'*30)
    if cont == "N":
        break

#quantas pessoas foram cadastradas?
print(f'foram cadastradas um total de {len(group)} pessoas')

#listagem com pessoas mais pesadas:
for p in group:
    if p[1] > 90:
        maisp += 1
        print(f'{p[0]} está com {p[1]}kg, está acima do peso!')

#listagem mais leves
    elif p[1] < 60:
        print(f'{p[0]} está com {p[1]}kg, está abeixo do peso!')
        maisl += 1

print(f'\nForam cadastradas {maisp} pessoas acima do peso e {maisl} pessoas abaixo do peso!')