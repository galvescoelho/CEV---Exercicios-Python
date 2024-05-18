#exercicio 58
print('vamos descobrir hoje o sexo do bebe!')
print('---------------------')
sexo = str(input('é homem ou mulher? [m / f]: '))
while 'f' != sexo != 'm':
    print('escolha uma opção valida!')
    sexo = str(input('é homem ou mulher? [m / f]: '))
if sexo == 'm':
    print('obrigado por usar o baby simulator! seu filho será do sexo masculino!')
else:
    print('obrigado por usar o baby simulator, você terá uma filha linda!')