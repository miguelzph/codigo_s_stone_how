'''Questão 3'''

def ler_inteiro():
    '''Lê e retorna um número inteiro'''
    
    entrada = input('Qual o número? ')
    
    if not entrada.isdigit():
        print('\nA entrada não foi um número!\n')
        return ler_inteiro()
    
   
    return int(entrada)


def inverter_numero(numero):
    '''Inverte um número inteiro'''
    
    numero = str(numero)[::-1]
    
    return int(numero)


numero = ler_inteiro()
numero_invertido = inverter_numero(numero)

print(f'\nO número {numero} invertido é: {numero_invertido}')