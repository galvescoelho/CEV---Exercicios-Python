#exercicio 27
nome = str(input('como você se chama? ')).lower().strip()
print('seu nome é: {}'. format(nome.title()))
primeiro_nome = nome.split()
print('seu primeiro nome é: {}'. format(primeiro_nome[0]))
print('seu ultimo nome é: {}'. format(primeiro_nome[-1]))
