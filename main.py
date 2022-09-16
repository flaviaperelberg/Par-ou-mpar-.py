# Faça um algoritmo que leia um número inteiro e mostre uma mensagem indicando se este número é par ou ímpar, e se é positivo ou negativo.

numero = int(input('Olá, quer saber se um número inteiro é par ou impar? Quer saber se é positivo ou negativo? Digite o número abaixo e descubra: \n'))

if int((numero % 2) == 0):
  print('O número é par')
else:
  print ('o número é impar')

if int((numero >= 0)):
  print ('O número é positivo')
else:
  print('O número é negativo')