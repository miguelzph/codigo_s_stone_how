'''Exercício 4:

Faça um programa que imprima na tela se um dado ano é bissexto ou não de acordo com as regras na ordem abaixo:

Um ano que é divisível por 400 é bissexto.
Dos anos que não entram na regra 1, se o ano for divisível por 100 então ele não é bissexto.
Dos anos que não entram na regra 2, se o ano for divisível por 4 então ele é um ano bissexto.
Todos os outros anos não são bissextos
'''

ano = int(input('Digite o ano: '))

if ano % 400 == 0 or (ano % 100 != 0 and ano % 4 == 0):
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} NÃO é bissexto!')
