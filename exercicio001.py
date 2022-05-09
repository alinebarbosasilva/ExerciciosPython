preco = float(input('Digite o preço do produto: '))
percentualDesconto = float(input('Digite o percetual de desconto (0-100%): '))

desconto = preco * (percentualDesconto / 100)
final = preco - desconto

print('O preço do produto é {}. Desconto de {}%.' .format(preco, percentualDesconto))
print('Valor calculado de desconto: {}. Valor final do produto {}' .format(desconto, final))