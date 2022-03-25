"""
Uma cartela de BINGO consiste em 5 colunas de 5 números que são rotulados com as letras B, I, N, G e O.
Atenção: Google it, para quem nunca viu uma cartela dessas!

Existem 15 números que podem aparecer sob cada letra respeitando a regra abaixo.
- B -> números variando de 1 a 15  (inclusos)
- I -> números variando de 16 a 30 (inclusos)
- N -> números variando de 31 a 45 (inclusos)
- ... e assim por diante

Passo número 0:
- Escreva uma função que crie uma cartela de BINGO aleatória. Dica(podemos usar um dicionário!). 
- As chaves serão as letras B, I, N, G e O. 
- Os valores serão as listas de cinco números aleatórios respeitando a regra dos intervalos de cada letra. 

Passo número 1: 
- Escreva uma segunda função que exiba a cartela de BINGO com as colunas rotuladas apropriadamente
- Formate a saída no terminal para que a cartela seja impressa em forma de colunas (letras e seus valores abaixo)

Passo número 2: 
- Sorteie uma letra e número aleatório (respeitando a regra) e veja se a cartela contém aquele número.

Passo número 3:
- Sorteie 50 (letras e) números e verifique se a cartela é vencedora ou não.
- Uma cartela é vencedora quando preencher uma linha ou coluna inteira com números sorteados.

Passo número desafio:
- Simule 1.000 jogos que sorteiam TODOS os números até que uma mesma cartela seja preenchida e contabilize:
    * O número mínimo de sorteio para que a carteja seja vencedora (não necessariamente preencher toda a cartela!)
    * A média do número de sorteios para que a carteja seja vencedora
    * O número máximo de sorteios para que a cartela seja vencedora
"""


import random


def retornar_aleatorio(inicial: int, range_coluna: int) -> int:
    '''Retorna um valor aleátorio'''
    return random.choice(range(inicial, inicial+range_coluna)) 


def adicionar_coluna(inicial: int, range_coluna: int, tamanho: int = 5) -> list:
    '''Cria e retorna uma lista de números aleátorios'''
    lista_coluna = []
    
    while True:
        
        # aleatorio
        aleatorio = retornar_aleatorio(inicial, range_coluna)
        
        # adicionando se nao houver
        if aleatorio not in lista_coluna:
            lista_coluna.append(aleatorio)
        else:
            continue
        
        # se preencheu tudo --> sai do while
        if len(lista_coluna) == tamanho:
            break
    
    return lista_coluna


def criar_cartela(inicial: int = 1, range_coluna:int = 15, lista_letras: list or None = None, num_colunas:int = 5) -> dict:
    '''Cria uma cartela de bingo'''
    dic_cartela = dict()
    
    if lista_letras is None:
        lista_letras = ['B', 'I', 'N', 'G', 'O']
    
    for letra in lista_letras:
        dic_cartela[letra] = (sorted(adicionar_coluna(inicial, range_coluna)))
        
        inicial += range_coluna
        
    return dic_cartela


def cartela_para_records(cartela:dict) -> list:
    '''Recebe uma tabela dicionário no formato chave:lista e retorna em formato json(records)'''
    
    json_cartela = []
  
    for i in range(len(cartela)):
        dic_linha = {chave: valor[i] for chave, valor in cartela.items()}
        json_cartela.append(dic_linha)
    
    return json_cartela

def printar_cartela(cartela:list) -> None:
    '''Printa a cartela'''
    
    cartela_linhas = cartela_para_records(cartela)
    
    # titulo
    print('   '.join(list(cartela_linhas[0].keys())))
    
    # valores
    for linha in cartela_linhas:
        print('  '.join([str(valor).zfill(2) for valor in linha.values()]))
        
    return None

def sortear_numero(valores_restantes:list) -> list:
    '''Sorteia e retira um número de uma lista de possíveis números'''
    valor_sorteado = random.choice(valores_restantes)
    
    valores_restantes.remove(valor_sorteado)
    
    return valor_sorteado, valores_restantes


def alterar_cartela(cartela:dict, num_sorteado:int) -> dict:
    '''Confere e preeche a cartela se o número estiver contido'''
    # conferir e alterar coluna
    for chave, coluna in cartela.items():
        cartela[chave] = [num if num!=num_sorteado else 'XX' for num in coluna]
        
    return cartela


def verificar_vitoria(cartela:dict) -> bool:
    '''Verifica se a cartela é vencedora ou não'''
    
    # verificando colunas
    for coluna in cartela.values():
        if coluna.count('XX') == len(coluna):
            return True
        
    # verificando linhas
    cartela_linhas = cartela_para_records(cartela)        
    for linha in cartela_linhas:
        if list(linha.values()).count('XX') == len(linha):
            return True
        
    return False


def jogar_bingo(cartela:dict or None=None, qtd_sort:int=75, parar_ao_vencer:bool=True, cartelas_info:bool=False)->bool or int:
    ''' Executa o jogo do bingo
    
        qtd_sort: qtd de sorteios realizados
        parar_ao_vencer: parar ou não ao vencer, esse paramêtro altera o retorno da função
        cartelas_info: printar as cartelas intermediárias para cada número sorteado
    
        Retorna True ou False, porém quando o parar_ao_vencer=True, retorna o número de vezes
        necessárias para alcançar a vitória'''
    
    # caso não passe uma cartela
    if cartela is None:
        cartela = criar_cartela()
    
    # possíveis valores a serem sorteados no jogo
    possiveis_valores = list(range(1, 15 * len(cartela)+1))
    
    for i in range(1, qtd_sort+1):
        
        # sorteio
        num_sorteado, valores_restantes  = sortear_numero(possiveis_valores)
        
        # serve para comparar e imprimir
        cartela_anterior = cartela.copy()
        
        # confere e altera caso haja o número sorteado
        cartela = alterar_cartela(cartela, num_sorteado)
        
        # printa a tabela a cada número sorteado
        if cartelas_info:
            print('\n============================')
            print(f'SORTEIO DE NÚMERO {i}')
            if cartela_anterior != cartela:
                print(f'O número {num_sorteado} ESTÁ na cartela\n')
            else:
                print(f'O número {num_sorteado} NÃO ESTÁ na cartela\n')
            printar_cartela(cartela)
        
        # para ao vencer e retorna i vezes que levou para isso
        if parar_ao_vencer:
            if verificar_vitoria(cartela):
                return i
    
    return verificar_vitoria(cartela)



### PASSO 1 ###

print('\n########################## PASSO 1 ##########################')
print('\n')
cartela1 = criar_cartela()
printar_cartela(cartela1)


### PASSO 2 ###

print('\n########################## PASSO 2 ##########################')
jogar_bingo(cartela1.copy(), qtd_sort=1, parar_ao_vencer=False, cartelas_info=True)


### PASSO 3 ###

print('\n########################## PASSO 3 ##########################')

if jogar_bingo(cartela1.copy(), qtd_sort=50, parar_ao_vencer=False, cartelas_info=True):
    print('\nA cartela é vencedora!\n')
else:
    print('\nA cartela NÃO é vencedora!\n')

     
### PASSO 4 ###

print('\n########################## PASSO 4 ##########################')
lista_qtd_necessaria_vitoria = []
for _ in range(1000):
    lista_qtd_necessaria_vitoria.append(jogar_bingo(cartela1.copy(), parar_ao_vencer=True))
    
print(f'''* O número mínimo de sorteios para que a carteja seja vencedora: {min(lista_qtd_necessaria_vitoria)}
* A média do número de sorteios para que a carteja seja vencedora: {sum(lista_qtd_necessaria_vitoria)/len(lista_qtd_necessaria_vitoria):.1f}
* O número máximo de sorteios para que a cartela seja vencedora: {max(lista_qtd_necessaria_vitoria)} 

''')

