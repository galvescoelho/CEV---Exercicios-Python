#exercicio 56
print('serviço de cadastro do ibge')
print('iremos realizar umas perguntas sobre vocês!')
print('-=-'*15)
idades = 0
homens = 0
idade_homem = 0
idoso = ''
menor_idade = 0
for ibge in range(1, 5):
    nome = str(input('como você se chama? ')).capitalize()
    idade = int(input('qual a sua idade? '))
    genero = str(input('qual o seu genero? \033[34m{mas / fem)\033[m ')).lower()
    idades += idade
    if genero == 'mas':
        homens += 1
        if homens == 1:
            idade_homem = idade
            idoso = nome
        else:
            if idade > idade_homem:
                idade_homem = idade
                idoso = nome
    elif genero == 'fem':
        if idade <= 19:
            menor_idade += 1

    print('----------------------------')
print('a media da idades do grupo é de: {}'.format(idades/4))
print('o homem mais velho é o {} com {} anos'.format(idoso, idade_homem))
print('total de mulheres com menos de 20: {}'.format(menor_idade))
