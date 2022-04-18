'''Questão 1'''

def ler_km():
    
    entrada = input('Quantos km foram percorridos? ')
    
    try:
        entrada = float(entrada)
    
    except ValueError:
        print('\nA entrada não foi um número!\n')
        return ler_km()
    
    if entrada == 0:
        print('\nEntrou tem que pagar!\n')
    
    return entrada
    
def calcular_tarifa(tarifa_basica: float = 4.0,
                    tarifa_variavel: float = 0.25,
                    metragem_tarifa_variavel: int = 140) -> float:
    
    '''calcula a tarifa a partir de parametros passados'''
    
    distancia_km = ler_km()
    
    distancia_metro = distancia_km * 1000
    
    valor_tarifa = tarifa_basica + tarifa_variavel * (distancia_metro / metragem_tarifa_variavel)
    
    print(f'O valor da tarifa é de R$ {valor_tarifa:.2f}')
    
    return None

calcular_tarifa()