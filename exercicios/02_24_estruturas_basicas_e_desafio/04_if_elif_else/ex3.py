'''Exercício 3:

A tabela a seguir lista os níveis sonoros em decibéis para alguns barulhos comuns
Barulho
Nível sonoro (dB)
Britadeira
130
Cortador de grama
106
Despertador
70
Cômodo em silêncio
40



Escreva um programa que leia um valor de nível sonoro do usuário em decibéis. 
Se o valor for um dos que estão na tabela, o programa deve retornar aquele barulho.
Caso o número esteja entre algum dos valores da tabela, o programa deve dizer entre quais
barulhos o valor digitado está. Seu programa deve informar também quando o valor for menor 
que o ruído mínimo da tabela e maior que ruído máximo. 
'''
dic = {
    130: 'Britadeira',
    106: 'Cortador de grama',
    70: 'Despertador',
    40: 'Cômodo em silêncio'
}

max_nivel = max(dic.keys())
min_nivel = min(dic.keys())

decibeis_usuario = int(input('Digite o valor de nível sonoro'))

if decibeis_usuario in dic.keys():
    print(f'Este é o ruído equivalente a um(a) {dic[decibeis_usuario]}')
elif decibeis_usuario > max_nivel:
    print('Este ruído é maior que o ruído máximo')
elif decibeis_usuario < min_nivel:
    print('Este ruído é menor que o ruído mínimo')
else:
    if decibeis_usuario > list(dic.keys())[1]:
        print(f'O ruído é maior que o ruído de um(a) "{dic[list(dic.keys())[1]]}" e menor que o de um(a) "{dic[list(dic.keys())[0]]}"')
    elif decibeis_usuario > list(dic.keys())[2]:
        print(f'O ruído é maior que o de um(a) "{dic[list(dic.keys())[2]]}" e menor que o de um(a) "{dic[list(dic.keys())[1]]}"')
    else:
        print(f'O ruído é maior que o de um(a) "{dic[list(dic.keys())[3]]}" e menor que o de um(a) "{dic[list(dic.keys())[2]]}"')
        