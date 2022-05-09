#----------------COMEÇO DA FUNÇÃO dimensoesObjeto----------------
def dimensoesObjeto():
  while True:
   try:
    comprimentoObjeto = float(input('Digite o comprimento do objeto (em cm ): ')) #Recebe o comprimento do objeto
    larguraObjeto = float(input('Digite o largura do objeto (em cm): ')) #Recebe a largura do objeto
    alturaObjeto = float(input('Digite o altura do objeto (em cm): ')) #Recebe a altura do objeto
    calculoVolume = (comprimentoObjeto * larguraObjeto * alturaObjeto)
    if calculoVolume < 1000:
        return 10.00
    elif (calculoVolume <= 1000) and (calculoVolume < 10000):
        return 20.00
    elif (calculoVolume <= 10000) and (calculoVolume < 30000):
        return 30.00
    elif (calculoVolume <= 30000) and (calculoVolume < 100000):
        return 50.00
    else:
        print('O volume do objeto é (em cm³): {:.2f} \nNão aceitamos objetos com dimensões tão grandes' 
            '\nEntre com as dimensões desejados novamente'.format(calculoVolume))
        continue
   except ValueError:
       print('Você digitou alguma dimensão do objeto com valor não numérico. \nPor favor entre com as dimensões desejados novamente') #Tratamento de erro quando não digitado um valor não numérico
       continue
#--------------------FIM DA FUNÇÃO dimensoesObjeto---------------

#----------------COMEÇO DA FUNÇÃO pesoObjeto --------------------
def pesoObjeto():
  while True:
   try:
    pesoDoObjeto = float(input('Digite o peso do Objeto (em kg): ')) #Recebe o peso do objeto
    if pesoDoObjeto <= 0.1:
        return 1.0
    elif (pesoDoObjeto < 0.1) and (pesoDoObjeto <= 1.0):
        return 1.5
    elif (pesoDoObjeto < 1.0) and (pesoDoObjeto <= 10.0):
        return 2.0
    elif (pesoDoObjeto >= 10.0) and (pesoDoObjeto <= 30.0):
        return 3.0
    else:
        print('Não aceitamos objetos tão pesados'
              '\nEntre com o peso desejado novamente')  #Tratamento de objeto pesado
        continue
   except ValueError:
       print('Você digitou peso do objeto com valor não numérico. \nPor favor entre com o peso desejado novamente')
       continue
#--------------------FIM DA FUNÇÃO pesoObjeto -------------------

#----------------COMEÇO DA FUNÇÃO rotaObjeto --------------------
def rotaObjeto():
  while True:
    rotaEscolhida = input("Selecione a rota: \nBR - De Brasília para Rio de Janeiro \nBS - De Brasília para São Paulo"
                        "\nRB - De Rio de Janeiro para Brasília \nRS - De Rio de Janeiro para São Paulo \nSR - De São Paulo "
                        "para Rio de Janeiro \nSB - De São Paulo para Brasília\n>>") # Escolha de uma rota
    if rotaEscolhida == "BR":
        return 1.5
    elif rotaEscolhida == "BS":
        return 1.2
    elif rotaEscolhida == "RB":
        return 1.5
    elif rotaEscolhida == "RS":
        return 1.0
    elif rotaEscolhida == "SR":
        return 1.0
    elif rotaEscolhida == "SB":
        return 1.2
    else:
        print('Você digitou uma rota que não existe'
              '\nPor favor entre com a rota desejada novamente') #Tratamento de rota errada
        continue
#--------------------FIM DA FUNÇÃO rotaObjeto -------------------

#------------------COMEÇO DA  MAIN ------------------------
print('Bem Vindo a Companhia de Logistica Aline Barbosa Silva S.A.')
dimensoes = dimensoesObjeto()
peso = pesoObjeto()
rotas = rotaObjeto()
total = dimensoes * peso * rotas
print('Total a pagar(R$): {:.2f} (dimensões: {:.2f} * peso: {} * rota: {:.2f})' .format(total, dimensoes,peso,rotas)) #Recebe o total dos serviços selecionados a ser pago pelo cliente
#--------------------FIM DA  MAIN -------------------------