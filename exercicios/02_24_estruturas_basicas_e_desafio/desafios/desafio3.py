'''Desafio 3:
    
Duas palavras podem ser consideradas anagramas de si mesmas se as letras de uma 
palavra podem ser realocadas para formar a outra palavra. 
Dada uma string qualquer, desenvolva um algoritmo que encontre o número de 
pares de substrings que são anagramas.
'''





def resultado_fatorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * resultado_fatorial(numero-1)
        
    
# ENTRADA
palavra = input('Digite a palavra: ')

tamanho_palavra = len(palavra)


# populando um dicionario com as frequencias de cada letra
dic_frequencia_letras = {}

for letra in palavra:
    if letra in dic_frequencia_letras.keys():
        dic_frequencia_letras[letra] +=1
    else:
        dic_frequencia_letras[letra] = 1

        
# FORMULA --> https://pt.wikipedia.org/wiki/Anagrama
#     Topico de Análise combinatória


# formula inicial (ao final será tirado o 1)
numero_de_pares = resultado_fatorial(tamanho_palavra)

# caso de letras repetidas
for valor in dic_frequencia_letras.values():
    if valor != 1:
        numero_de_pares = (numero_de_pares / resultado_fatorial(valor))

# removendo a propria palavra --> dúvida se preciso ou não retirar esse 1
numero_de_pares -= 1
        

print(f'\nA palavra {palavra} possui {numero_de_pares} pares de substring que são anagramas.')