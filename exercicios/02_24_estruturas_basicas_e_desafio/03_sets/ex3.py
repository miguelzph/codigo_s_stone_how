'''Exercício 3:

Faça um programa que ordene um dicionário por seus valores. Exemplo: dado o dicionário
>>> {“matemática”: 81, “física”: 83, “química”: 87} 
a saída deve ser 
>>> {“química”: 87, “física”: 83, matemática”: 81}

'''
def func_aux_ordenar(item):
    return item[1]

dic = {'matemática': 81, 'física': 83, 'química': 87}

dic_ordenado  = dict(sorted(dic.items(), key=func_aux_ordenar, reverse=True))

print(f'O dicionário ordenado é: {dic_ordenado}')