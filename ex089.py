lista = []
c = 0
while True:
    print('-'*30)
    nome = str(input('digite um nome: '))
    nota1 = float(input('nota 1: '))
    nota2 = float(input('nota 2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome,[nota1, nota2], media]
    c += 1
    cont = str(input('Quer adicionar mais alguem?[S/N] '))
    if cont in 'nN':
        break
print('-'*26)
print(f'{"No°":>3}{"Aluno":>10}{"NOTA":>10}')
for p, i in enumerate(lista):
    print(f'{p:>3}{lista[p][0]:<10}{lista[p][2]:>10.2f}')
while True:
    escolha = int(input('Quer ver as notas de qual aluno? '))
    if escolha == 999:
        break
    elif escolha <= c:
        print(f'As notas de {lista[escolha][0]} foram: {lista[escolha][1]}')
print('Finalizando...')
print('<<< VOLTE SEMPRE >>>')