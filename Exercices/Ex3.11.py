preco = float(input('Digite o preço da mercadoria: '))
perc = int(input('Digite o percentual de desconto: '))

_novoprec = (preco - (preco * perc / 100))
_desconto = preco - _novoprec

print('O valor do desconto R${:.2f}\n'
      'Novo preço a pagar R${:.2f}'.format(_desconto, _novoprec))
