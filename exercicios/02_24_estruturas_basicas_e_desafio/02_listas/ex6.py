'''Exercício 6:

Faça um programa que remova strings vazias de uma lista de strings. Exemplo: dada a 
lista [“Olá”, “”, “meu”, “nome”, “”, “é”, “facilitador”, “”] a saída deve ser
>>> [“Olá”, “meu”, “nome”, “é”, “facilitador”]
'''

lista = ['Olá', '', 'meu', 'nome', '', 'é', 'facilitador', '']
string = ' '.join(lista)
nova_lista = string.split()
print(f'A nova lista é: {nova_lista}')