s = 0
mdm = 0
mais_b = 0
mais = ''
item_mb = ''
print('----------------------------')
print('     Loja Super Baratão     ')
print('----------------------------')
item = str(input('Nome do produto: '))
cost = float(input('Preço: '))
s += cost
if cost >= 1000:
    mdm += 1
mais_b = cost
item_mb = item
while True:
    while 'S' != mais != 'N':
        mais = str(input('Quer continuar? [S/N] ').upper())
    if mais == 'N':
        break
    print('----------------------------')
    item = str(input('Nome do produto: '))
    cost = float(input('Preço: '))
    s += cost
    if cost >= 1000:
        mdm += 1
    elif cost < mais_b:
        mais_b = cost
        item_mb = item
    mais = ''
print(f'O total da compra foi de {s:3}')
print(f'temos {mdm} produtos custando mais de: R$ 1 mil')
print(f'o produto mais barato foi {item_mb} custando R$ {mais_b}')
