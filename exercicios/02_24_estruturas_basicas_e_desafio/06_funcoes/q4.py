'''Questão 4'''

from itertools import permutations
from random import choice

def ler_palavra():
    '''Lê e retorna um número inteiro'''
    
    palavra = input('Qual é a palavra? ')
    
    if not (palavra.isalpha()) or (len(palavra.split()) != 1):
        print('\nA entrada não foi uma palavra!\n')
        return ler_palavra()
    
   
    return palavra.lower()

def devolver_palavra_embaralhada(palavra):
    '''Devolve uma palavra embaralhada'''
    
    escolhas_possiveis = tuple(permutations(palavra))
    
    palavra_selecionada = choice(escolhas_possiveis)                        
                               
    return ''.join(palavra_selecionada)
                               
palavra = ler_palavra()
palavra_embaralhada = devolver_palavra_embaralhada(palavra)

print(f'\nA palavra "{palavra}" embaralhada aleatoriamente é: {palavra_embaralhada}')