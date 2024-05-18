#exercicio 22
nome = str(input('escreva seu nome completo: ')).strip().lower()
print(nome.lower())
print(nome.upper())
print('seu nome tem \033[34m{} \033[mletras!'.format(len(nome.replace(' ', ''))))
nomes = nome.split()
print('seu primeiro nome tem \033[34m{}\033[m letras'.format(len(nomes[0])))