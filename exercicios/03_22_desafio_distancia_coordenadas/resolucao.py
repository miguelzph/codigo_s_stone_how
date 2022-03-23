'''A superfície da Terra é curva, e a distância entre os graus de longitude varia com a latitude.
Como resultado, encontrar a distância entre dois pontos na superfície da Terra é mais complicado do que simplesmente usar o teorema de Pitágoras.
Sejam (t1, g1) e (t2, g2) a latitude e a longitude de dois pontos na superfície da Terra.
A distância entre esses pontos, acompanhando a superfície da Terra, em quilômetros é:

distancia = 6371,01 x arccos(sen(t1) x sen(t2) + cos(t1) x cos(t2) x cos(g1 - g2))

O valor 6371,01 na equação anterior não foi selecionado aleatoriamente. 
É o raio médio da Terra em quilômetros.

Crie um programa que permita ao usuário inserir a latitude e longitude de dois pontos da Terra em graus.
Seu programa deve exibir a distância entre os pontos, seguindo a superfície da terra, em quilômetros.

Dica¹: as funções trigonométricas do Python operam em radianos. 
Como resultado, você vai precisa converter a entrada do usuário de graus para radianos antes de calcular a distância com a fórmula discutida anteriormente. 
O módulo math contém um função chamada radianos que converte de graus para radianos.

Dica²: 
Latitude varia de -90° (sul) até +90° (norte). O ponto de latitude 0° é a linha do equador
Longitude varia de -180° (leste) até +180° (oeste). O ponto de longitude 0° é o meridiano de Greenwich'''



from math import radians, sin, cos, acos

def eh_float(valor):
    '''Verifica se um número é float, e retorna True ou False'''
    try:
        valor = float(valor)
        return True
    except:
        return False

def ler_valor(nome_do_ponto, tipo_valor='latitude', limite_inf=-90, limite_sup=90):
    '''Lê um valor do usuário e verifica se é valido'''
    valor = input(f'Digite a {tipo_valor} do {nome_do_ponto}: ')
    
    # confere se é float
    if not eh_float(valor):
        print(f'Valor de {tipo_valor} inválido!! Digite um número!')
        return ler_valor(nome_do_ponto, tipo_valor, limite_inf, limite_sup) 
    else:
        valor = float(valor)
    
    # confere os limites do valor
    if not (limite_inf <= valor <= limite_sup) :
        print(f'Valor de {tipo_valor} inválido!! Digite um valor entre {limite_inf} e {limite_sup}\n')
        # chama a função novamente
        return ler_valor(nome_do_ponto, tipo_valor, limite_inf, limite_sup) 
    
    return valor


def ler_ponto(nome_do_ponto):
    '''Lê a latitude e a longitude de um ponto, e retorna-os em um dicionário'''
    
    latitude = ler_valor(nome_do_ponto)
    
    longitude = ler_valor(nome_do_ponto, tipo_valor='longitude', limite_inf=-180, limite_sup=180)
    
    return {'lat': latitude, 'long': longitude}


def converter_radianos(dic):
    '''Converte todos os valores de um dicionário de graus para radianos'''
    return {'lat': radians(dic['lat']), 'long': radians(dic['lat'])}


def calcular_distancia(p1, p2):
    '''Calcula distância entre dois pontos dados em formato de dicionário'''
    raio_terra = 6371.01
    distancia = raio_terra * ( acos( sin(p1['lat']) * sin(p2['lat']) + cos(p1['lat']) 
                           * cos(p2['lat']) * cos(p1['long'] - p2['long']) ) )
    return distancia


##### Código
# leitura dos pontos 
ponto1, ponto2 = ler_ponto('Ponto 1'), ler_ponto('Ponto 2')

# converte os pontos para radianos
ponto1, ponto2 = converter_radianos(ponto1), converter_radianos(ponto2)

distancia_final = calcular_distancia(ponto1, ponto2)

print(f'A distância entre os dois pontos é de {distancia_final:.2f} KM')