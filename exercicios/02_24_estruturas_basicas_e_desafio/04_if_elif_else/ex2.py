'''Exercício 2:

Escreva um programa que receba dois números e imprima na tela se o primeiro é divisível pelo segundo.
'''

primeiro_numero = int(input('Digite o primeiro número: '))

segundo_numero = int(input('Digite o segundo número: '))

if primeiro_numero % segundo_numero == 0:
    print(f'O número {primeiro_numero} é divisível por {segundo_numero}!')
else:
    print(f'O número {primeiro_numero} NÃO é divisível por {segundo_numero}!')