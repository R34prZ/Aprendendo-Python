#selecionar opera��o
operacao = input('Escolha a opera��o: ')
num1 = float(input('Primeiro n�mero: '))
num2 = float(input('Segundo n�mero: '))
num = [num1 , num2]

#definindo as poss�veis opera��es
def soma(num):
  soma = num1 + num2
  print('A resposta �', soma)
  
def subt(num):
  subt = num1 - num2
  print('A resposta �', subt)

def mult(num):
  mult = num1 * num2
  print('A resposta �',mult)

def div(num):
  div = num1 / num2
  print('A resposta �', div)

#dando os resultados
if operacao == 'soma':
  soma(num)

elif operacao == 'subtra��o':
  subt(num)

elif operacao == 'multiplica��o':
  mult(num)

elif operacao == 'divis�o':
  div(num)
  
#em caso de uma palavra n�o esperada ser inserida em operacao
else:
  print('Ops! \nVoc� deve ter selecionado a opera��o errada, tente novamente utilizando os termos "soma", "subtra��o", "multiplica��o" ou "divis�o"')