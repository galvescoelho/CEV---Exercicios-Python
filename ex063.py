#exercicio 63
print('então vamos de fibonacci')
n = int(input('quantos elementos de fibonacci você quer? '))
t1 = 0
t2 = 1
t3 = 0
f = 3
print('---------------')
print('{} → {}'.format(t1, t2), end='')
while f < n+1:
    t3 = t1 + t2
    print(' → {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    f += 1
print(' → fim')
