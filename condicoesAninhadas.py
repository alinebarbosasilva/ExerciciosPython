#exercicio 4.1.1

print('escolha o que deseja comprar:')
print('1 - maça')
print('2 - laranja')
print('3 - banana')
produto = int(input('qual sua sua escolha?'))
qtd = int(input('quantas unidades'))
if(produto == 1):
    pagar = qtd * 2.3
    print('você comprou {} maças. total a pagar: {}' .format(qtd, pagar))
else:
    if(produto == 2):
        pagar = qtd * 3.6
        print('você comprou {} laranjas. total a pagar: {}'.format(qtd, pagar))
    else:
     if(produto == 3):
        pagar = qtd * 1.85
        print('você comprou {} bananas. total a pagar: {}'.format(qtd, pagar))
     else:
         print('produto inexistente')


#utilizando o elif

print('escolha o que deseja comprar:')
print('1 - maça')
print('2 - laranja')
print('3 - banana')
produto = int(input('qual sua sua escolha?'))
qtd = int(input('quantas unidades'))
if(produto == 1):
   pagar = qtd * 2.3
   print('você comprou {} maças. total a pagar: {}' .format(qtd, pagar))
elif(produto == 2):
    pagar = qtd * 3.6
    print('você comprou {} laranjas. total a pagar: {}'.format(qtd, pagar))
elif(produto == 3):
    pagar = qtd * 1.85
    print('você comprou {} bananas. total a pagar: {}'.format(qtd, pagar))
else:
    print('produto inexistente!')


#exercício

nome = input('qual seu nome?')
idade = int(input('qual a sua idade?'))
if nome == 'vinicius':
    print('olá, vinicius!')
elif idade < 18:
    print('você não é o vinicius! e é menor de idade!')
elif idade > 100:
    print('diferente de você, o vinicius não é imortal')


print(1387 // 19)

print(31 % 2 == 0)

if(idade > 60):
    print('Você tem direito aos beneficios!')

dano = 12
escudo = 0
if(dano > 10 and escudo == 0):
    print('Você está morto!')




