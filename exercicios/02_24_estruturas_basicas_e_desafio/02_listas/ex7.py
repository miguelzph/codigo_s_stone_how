'''Exercício 7:

Dada a lista de strings [“1”, “7”, “99”, “15”] construa um programa que converte todos os 
elementos desta lista para inteiro.

Faça também o inverso, dada a mesma lista só que agora de elementos inteiros, 
converta todos os elementos para str.
'''
#lista = ['1', '7', '99', '15']
lista = [1, 7, 99, 15]
if type(lista[0]) is int:
    lista_final = list(map(str, lista))
else:
    lista_final = list(map(int,lista))

print(f'A lista final convertida é:{lista_final}')