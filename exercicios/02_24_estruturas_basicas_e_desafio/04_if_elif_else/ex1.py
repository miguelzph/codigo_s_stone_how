'''Exercício 1:

Escreva um programa que diga se um número dado pelo usuário é par ou ímpar
'''

numero_usuario = int(input('Digite o número: '))

if numero_usuario % 2 == 0:
    print(f'O número {numero_usuario} é PAR!')
else:
    print(f'O número {numero_usuario} é ÍMPAR!')