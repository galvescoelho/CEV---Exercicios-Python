#exercicio 40
print('escola santa paciencia!')
print('Este é o serviço de boletim digital. Vamos conferir se você passou de ano!')
print('------------------------')
aluno = str(input('como você se chama, querido aluno(a)? '))
n1 = float(input('certo, {} nos conte quanto você tirou na Av1: '.format(aluno.title())))
n2 = float(input('e quanto você tirou na Av2? '))
media = (n1 + n2)/2
if media < 5:
    print('\033[31mComo você não alcançou o minimo de 5 para ter direito a recuperação, Foi reprovado\033[m!')
elif media >= 5 and media <= 6.9:
    print('\033[33mAtenção! Você teve uma media de {} e ainda não foi aprovado! agende a Av. de recuperação com o professor.\033[m'.format(media))
else:
    print('\033[32mParabéns {}, Sua nota foi {}, e é mais do que suficiente para iniciar suas ferias hoje!\033[m'.format(aluno, media))
print('------------------------')
print('obrigado por usar nosso boletim digital! Boa sorte e até ano que vem.')
