'''Exercício 2:

Faça um programa que lê uma sigla de um estado do usuário e imprime na tela o nome completo do estado. Exemplo:

>>> Digite um estado: SP
>>> O nome completo do estado é São Paulo.

'''
dic_estados = {
    'AC': 'Acre',
    'AL': 'Alagoas',
    'AP': 'Amapá',
    'AM': 'Amazonas',
    'BA': 'Bahia',
    'CE': 'Ceará',
    'DF': 'Distrito Federal',
    'ES': 'Espírito Santo',
    'GO': 'Goiás',
    'MA': 'Maranhão',
    'MT': 'Mato Grosso',
    'MS': 'Mato Grosso do Sul',
    'MG': 'Minas Gerais',
    'PA': 'Pará',
    'PB': 'Paraíba',
    'PR': 'Paraná',
    'PE': 'Pernambuco',
    'PI': 'Piauí',
    'RJ': 'Rio de Janeiro',
    'RN': 'Rio Grande do Norte',
    'RS': 'Rio Grande do Sul',
    'RO': 'Rondônia',
    'RR': 'Roraima',
    'SC': 'Santa Catarina',
    'SP': 'São Paulo',
    'SE': 'Sergipe',
    'TO': 'Tocantins'
}

sigla_usuario = input('Digite a sigla do estado (Ex: SP): ').upper()

if sigla_usuario in dic_estados.keys():
    print(f'\nO nome completo do estado é {dic_estados[sigla_usuario]}.')
else:
    print(f'\nNão existe um estado com a sigla "{sigla_usuario}"!')