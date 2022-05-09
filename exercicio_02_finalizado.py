subtotal = 0  # Recebe a soma dos valores dos produtos a ser pago pelo cliente
print('Bem Vindo a Lanchonete da Aline Barbosa Silva')
print('*****************Cardápio******************')
print('| Código |         Descrição      |  Valor |')
print('|  100   |   Cachorro Quente      |  9,00  |')
print('|  101   | Cachorro Quente Duplo  |  11,00 |')
print('|  102   |         X-Egg          |  12,00 |')
print('|  103   |         X-Salada       |  12,00 |')
print('|  104   |         X-Bacon        |  14,00 |')
print('|  105   |         X-Tudo         |  17,00 |')
print('|  200   |    Refrigerante Lata   |   5,00 |')
print('|  201   |        Chá Gelado      |   4,00 |')
while True:
    codigo = input('Entre com o código desejado: ')  # Escolha de um produto e inserido o código
    if codigo == '100':
      subtotal += 9.00 # Guarda o valor final de serviços pedidos
      print('Você pediu um Cachorro Quente no valor de 9.00')
    elif codigo == '101':
      subtotal += 11.00
      print('Você pediu um Cachorro Quente Duplo  no valor de 11.00')
    elif codigo == '102':
      subtotal += 12.00
      print('Você pediu um X-Egg  no valor de 12.00')
    elif codigo == '103':
      subtotal += 12.00
      print('Você pediu um X-Salada  no valor de 12.00')
    elif codigo == '104':
      subtotal += 14.00
      print('Você pediu um X-Bacon  no valor de 14.00')
    elif codigo == '105':
      subtotal += 17.00
      print('Você pediu um X-Tudo  no valor de 17.00')
    elif codigo == '200':
      subtotal += 5.00
      print('Você pediu um Refrigerante Lata  no valor de 5.00')
    elif codigo == '201':
      subtotal += 4.00
      print('Você pediu um Chá Gelado no valor de 4.00')
    else:
      print("Opção Inválida")
      continue
    opcao = input('Deseja pedir mais alguma coisa? 1 - Sim \n'
                    '0 - Não ')  #Finalizar compra ou continuar selecionando
    if opcao == '1':
      continue
    else:
        print('O total a ser pago é: {:.2f}' .format(subtotal))
        break
