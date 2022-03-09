'''Exercício 4:

Escreva um programa para encontrar o tamanho do comprimento das strings nos valores de dicionário. 
Exemplo: dada o dicionário
>>> {1: “vermelho”, 2: “azul”, 3: “marrom”}
A saída deverá ser
>>> {1: 8, 2: 4, 3: 6}

'''

dic_cores = {1: 'vermelho', 2: 'azul', 3: 'marrom'}

tamanho_cores = map(len, dic_cores.values())

novo_dic = dict(zip(dic_cores.keys(), tamanho_cores))

print(f'O novo dicionário é: {novo_dic}')