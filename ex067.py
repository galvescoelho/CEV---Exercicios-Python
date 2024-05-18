#exercicio 67
print('bem vindo a tabuada simulator!')
t = 1
num = int(input('você quer a tabuada de qual valor? '))
while True:
    print(f'{num} x {t:2} = {num*t}')
    t += 1
    if t == 11:
        print('------------------------')
        t = 1
        num = int(input('você quer a tabuada de qual valor? '))
    elif num < 0:
        break