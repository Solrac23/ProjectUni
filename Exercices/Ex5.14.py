s = 0  # Contador para a soma
cont = 0  # Contador
while True:
    num = int(input('Digite um valor(para sair digite 0): '))
    if num == 0:
        break
    s += num
    cont += 1
    ma = s / cont

print('Quantidade de nímero digítados: {}'.format(cont))
print('A soma dos números: {}'.format(s))
print('A média aritmética: {:.0f}'.format(ma))
