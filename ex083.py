#exercicio 83
conta = []
expr = str(input('digite a expressão: '))

for c in expr:
    if c == '(':
        conta.append('(')
    elif c == ')':
        if len(conta) > 0:
            conta.pop()
        else:
            conta.append(')')

if len(conta) == 0:
    print('a conta está correta')
else:
    print('a conta está incorreta!')

