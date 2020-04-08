cédulas = 0
while True:
    valor = int(input("Digite o valor a pagar:"))
    atual = 50
    apagar = valor
    if valor == 0:
        break
    while True:
        if atual <= apagar:
            apagar -= atual
            cédulas += 1
        else:
            print("%d cédula(s) de R$%d" % (cédulas, atual))
            if apagar == 0:
                break
            if atual == 50:
                atual = 20
            elif atual == 20:
                atual = 10
            elif atual == 10:
                atual = 5
            elif atual == 5:
                atual = 1
            cédulas = 0
