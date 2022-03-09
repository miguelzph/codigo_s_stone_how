'''Exercício 5:

Escreva um programa que receba uma string e diga se ela tem o formato de uma 
placa veicular brasileira (no formato antigo) com três letras, um traço e quatro números. Exemplos: 
Dada a entrada ABT-1234 o programa deveria exibir True
Dada a entrada JKL9999 o programa deveria exibir False
Qualquer outra entrada que fuja do padrão de 3 letras, um traço e quatro números, o programa deverá exibir False 
'''
placa = input('Digite a placa no formato ZZZ-0000: ').upper()
retorno_usuario = False

if len(placa) == 8 and '-' in placa:
    letras = placa[:placa.find('-')]
    numeros = placa[placa.find('-') + 1:]
    if letras.isalpha() and numeros.isdigit():
        retorno_usuario = True
        
print(retorno_usuario)