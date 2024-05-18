#exercicio 89
l_alunos = []
aluno = []
while True:
    print('-' * 30)
    nome = str(input('Como o aluno se chama? ').title())
    aluno.append(nome)
    av_um = float(input('Nota 1: '))
    aluno.append(av_um)
    av_do = float(input('Nota 2: '))
    aluno.append(av_do)
    l_alunos.append(aluno[:])
    aluno.clear()
    while True:
        cont = str(input('Quer adicionar mais alguem?[S/N] ').upper())
        if cont == 'S' or cont == 'N':
            break
        else:
            print('Digite "S" para sim, "N" para não.')
    if cont == 'N':
        break
print('-'*30)
print(f'{"No°":^5}{"NOME":<10}{"NOTA":>11}')
print('-'*30)
for aluno in l_alunos:
        media = (aluno[1]+aluno[2]) /2
        print(f'{l_alunos.index(aluno):^5}{aluno[0]:<10} {media:>10.2f}')
while True:
    print('-' * 30)
    conf = int(input('Mostrar as notas de qual aluno? '))
    if conf > len(l_alunos) and conf < 998:
        print('Não temos esse aluno em nossos registros.')
    elif conf <= len(l_alunos):
            print(f'Notas de {l_alunos[conf][0]} são: {l_alunos[conf][1]} e {l_alunos[conf][2]} ')
    elif conf == 999:
        break
print('Finalizando...')
print('<<< VOLTE SEMPRE >>>')