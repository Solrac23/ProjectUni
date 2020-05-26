"""Escreva um programa para controlar uma pequena máquina registradora.
Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada.
Utilize a tabela de códigos abaixo para obter o preço de cada produto:
Código Preço
1       0,50
2       1,00
3       4,00
5       7,00
9       8,00
Seu programa deve exibir o total das compras depois que o usuário digitar 0.
Qualquer outro código deve gerar a mensagem de erro “Código inválido”."""
print('=-=' * 7)
print('Código   Preço\n'
       '|1    |  0,50|\n'
       '|2    |  1,00|\n'
       '|3    |  4,00|\n'
       '|5    |  7,00|\n'
       '|9    |  8,00|')
print('=-=' * 7)

cod = 0
while True:
    prod = int(input('Digite o código do produto: '))
    if prod == 1:
        quant = int(input('Digite a quantidade de produtos: '))
        cod += 0.50 * quant
    elif prod == 2:
        quant = int(input('Digite a quantidade de produtos: '))
        cod += 1.00 * quant
    elif prod == 3:
        quant = int(input('Digite a quantidade de produtos: '))
        cod += 4.00 * quant
    elif prod == 5:
        quant = int(input('Digite a quantidade de produtos: '))
        cod += 7.00 * quant
    elif prod == 9:
        quant = int(input('Digite a quantidade de produtos: '))
        cod += 8.00 * quant
    elif prod == 0:
        print('Total a pagar: R$ {:.2f}'.format(cod))
        break
    else:
        print('Código inválido')
