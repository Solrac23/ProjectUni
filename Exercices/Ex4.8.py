n1 = int(input('Digite um número: '))

oper = input('Digite o operadores(+, -, *, /): ')

n2 = int(input('Digite o segundo número:'))

# Estrutura de condições
if oper == '+':
    soma = n1 + n2
    print("Soma: {} + {} = {}".format(n1, n2, soma))
elif oper == '-':
    sub = n1 - n2
    print('Subtração: {} - {} = {}'.format(n1, n2, sub))
elif oper == '*':
    mult = n1 * n2
    print('Multiplicação: {} * {} = {}'.format(n1, n2, mult))
elif oper == '/':
    div = n1 / n2
    print('Divisão: {} / {} = {:.2f}'.format(n1, n2, div))
else:
    print('Operador inválido!!')
