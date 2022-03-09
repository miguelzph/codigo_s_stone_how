'''Exercício 5:

Faça um programa que encontre as notas mínimas e máximas de um dicionário, e imprima-os na tela com as suas respectivas chaves. Exemplo: dado o dicionário
>>> {“Theodoro”: 20, “Márcia”: 50, “Júnior”: 80}
A saída deve ser
>>> Nota máxima -> Júnior : 80
>>> Nota mínima -> Theodoro : 20
'''
dic_notas = {'Theodoro': 20, 'Márcia': 50, 'Júnior': 80}

nota_maxima = max(dic_notas.values())
indice_nota_maxima = list(dic_notas.values()).index(nota_maxima)
pessoa_nota_maxima = list(dic_notas.keys())[indice_nota_maxima]

print(f'Nota máxima -> {pessoa_nota_maxima} : {nota_maxima}')

nota_minima = min(dic_notas.values())
indice_nota_minima = list(dic_notas.values()).index(nota_minima)
pessoa_nota_minima = list(dic_notas.keys())[indice_nota_minima]

print(f'Nota mínima -> {pessoa_nota_minima} : {nota_minima}')