print('Bem Vindo a Loja da Aline Barbosa Silva')

valor = float(input('Entre com o valor do produto: '))  # Recebe o valor total do produto a ser pago pelo cliente
quantidade = int(input('Entre com o valor da quantidade: '))  # Recebe a quantidade do produto

if quantidade <= 9:
    desconto = valor * 0.0
    preco = valor - desconto
    final = preco * quantidade
elif(quantidade >= 10) and (quantidade <= 99):
    desconto = valor * 0.05
    preco = valor - desconto
    final = preco * quantidade
elif(quantidade >= 100) and (quantidade <= 999):
    desconto = valor * 0.10
    preco = valor - desconto
    final = preco * quantidade
elif quantidade >= 1000:
    desconto = valor * 0.15
    preco = valor - desconto
    final = preco * quantidade
else:
    print('Produto Inválido!')
# valor sem desconto
print('O valor sem desconto foi: R$ {:.2f}.'.format(valor * quantidade))
print('O valor com desconto foi: R$ {:.2f}. (desconto {:.0f}%)' .format(final, desconto)) # valor aplicado o desconto e o desconto obtido
