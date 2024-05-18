#exercicio 69
s = ''
mais = ''
m_idade = 0
qntd_h = 0
menor_mulher = 0
print('serviço de cadastro ibge')
print('    VAMOS INICIAR!      ')
while True:
    print('----------------------')
    print('Cadastre uma pessoa')
    print('----------------------')
    idade = int(input('Idade: '))
    while 'M' != s != 'F':
        s = str(input('Sexo: \033[34mex[M/F] \033[m').upper())
    print('-------------------')
    while 'S' != mais != 'N':
        mais = str(input('quer continuar?[S/N] ').upper())
    if mais == 'N':
        break
    elif idade >= 18:
        m_idade += 1
    elif s == 'M':
        qntd_h += 1
    elif s == 'F' and idade < 20:
        menor_mulher += 1
print('----------------------')
print(f'a quantidade de maiores de idade foi igual a: {m_idade}')
print(f'a quantidade de homens registrados foi: {qntd_h}')
print(f'E a quantidade de mulheres com menos de 20 anos é de: {menor_mulher}')