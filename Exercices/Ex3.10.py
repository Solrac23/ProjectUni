
salario = float(input('Digite o seu salário: '))
aumento = int(input('Digite o valor do aumento: '))

_salarionov = (salario + (salario * aumento / 100))
_aumentsalario = _salarionov - salario

print("Valor de aumento R${:.2f}\n"
      "Novo salário a receber {:.2f}".format(_aumentsalario, _salarionov))
