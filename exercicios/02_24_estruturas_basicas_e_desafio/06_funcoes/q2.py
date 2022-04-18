'''Questão 2'''

from itertools import combinations

def ler_tamanho_reta(i: int):
    '''Lê o tamanho de uma reta e confere se é um número float
    
    i: referencial de que reta está sendo lida
    
    retorna o comprimento da reta'''
    
    entrada = input(f'Quantos tamanho da reta {i}? ')
    
    try:
        entrada = float(entrada)
    
    except ValueError:
        print('\nA entrada não foi um número!\n')
        return ler_tamanho_reta(i)
    
    return entrada


def eh_triangulo():
    '''Lê até 3 comprimentos de reta e verifica se é possível formar um triângulo
    
    retorna False durante a leitura se um dos valores invalidar o trinagulo
    
    retorna True ou False ao verificar a condição dos 3 lados do triângulo'''
    
    retas = []
    
    for i in range(1, 4):
        comp_reta = ler_tamanho_reta(i)
        
        if comp_reta <= 0:
            return False
        else:
            retas.append(comp_reta)
    
    
    combinacoes = tuple(combinations(retas, r=2))
    
    for comp_reta in retas:
        for comb in combinacoes:
            if comp_reta > sum(comb):
                return False
    
    return True


eh_triangulo()