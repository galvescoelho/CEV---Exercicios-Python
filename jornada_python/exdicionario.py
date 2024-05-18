#exercicio for dicionario
with open("vendasloja.txt", "r") as arquivo:
    textos = arquivo.read()
    lista_texto = textos.split('\n')

#somar faturamento dos valores gerados por venda
faturamento = 0
lista_texto.pop(0)
for linha in lista_texto:
    posição_pv = linha.find(';')
    valor = float(linha[posição_pv+1:])
    faturamento += valor
#formatando faturamento
print(f'o faturamento da loja foi de {faturamento:,.2f}')