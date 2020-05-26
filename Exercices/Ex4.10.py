# Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
# Pergunte a quantidade de kWh consumida e o tipo de instalação:
# R para residências, I para indústrias e C para comércios.
# Calcule o preço a pagar de acordo com a tabela a seguir.

faixa = int(input('Qual a quantidade consumida em kwh:'))
tipo = str(input('Tipo de instalação R(Residência), I(Indústrias) e C(Comércios):')).strip()[0]

if tipo == 'R' or tipo == 'r':
    if faixa <= 500:
        preco = faixa * 0.40
    elif faixa > 500:
        preco = faixa * 0.65
elif tipo == 'C' or tipo == 'c':
    if faixa <= 1000:
        preco = faixa * 0.55
    elif faixa > 1000:
        preco = faixa * 0.60
elif tipo == 'I' or tipo == 'i':
    if faixa <= 5000:
        preco = faixa * 0.55
    elif faixa > 5000:
        Preco = faixa * 0.60
else:
    print('Tipo de Instalação inválido!!')
print('Preço a pagar: R$ {:.2f}'.format(preco))
