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


def retornar_aleatorio(inicial, range_coluna):
    '''Retorna um valor aleátorio'''
    return random.choice(range(inicial, inicial+range_coluna)) 


def adicionar_coluna(inicial: int, range_coluna: int, tamanho=5):
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


def criar_cartela(inicial = 1, range_coluna=15, lista_letras=None, num_colunas=5):
    '''Cria uma cartela de bingo'''
    dic_cartela = dict()
    
    if lista_letras is None:
        lista_letras = ['B', 'I', 'N', 'G', 'O']
    
    for letra in lista_letras:
        dic_cartela[letra] = (sorted(adicionar_coluna(inicial, range_coluna)))
        
        inicial += range_coluna
        
    return dic_cartela


def cartela_para_records(cartela):
    '''Recebe uma tabela dicionário no formato chave:lista e retorna em formato json(records)'''
    
    json_cartela = []
  
    for i in range(len(cartela)):
        dic_linha = {chave: valor[i] for chave, valor in cartela.items()}
        json_cartela.append(dic_linha)
    
    return json_cartela

def printar_cartela(cartela):
    '''Printa a cartela'''
    
    cartela_linhas = cartela_para_records(cartela)
    
    # titulo
    print('   '.join(list(cartela_linhas[0].keys())))
    
    # valores
    for linha in cartela_linhas:
        print(', '.join([str(valor).zfill(2) for valor in linha.values()]))

def sortear_numero(valores_restantes):
    '''Sorteia o número o retirando de uma lista de possíveis números'''
    valor_sorteado = random.choice(valores_restantes)
    
    valores_restantes.remove(valor_sorteado)
    
    return valor_sorteado, valores_restantes


def preecher_cartela(cartela, num_sorteado):
    '''Confere e preeche a cartela se o número estiver contido'''
    # conferir e alterar coluna
    for chave, coluna in cartela.items():
        cartela[chave] = [num if num!=num_sorteado else 'XX' for num in coluna]
        
    return cartela


def verificar_vitoria(cartela):
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


def jogar_bingo(cartela, qtd_numeros=75, parar_ao_vencer=True, cartelas_verbose=False):
    ''' Executa o jogo do bingo
    
        Retorna True ou False, porém quando o parar_ao_vencer=True, retorna o número de vezes
        necessárias para alcançar a vitória'''
    
    possiveis_valores = list(range(1, 15 * len(cartela)+1))
    
    for i in range(1, qtd_numeros+1):
        
        num_sorteado, valores_restantes  = sortear_numero(possiveis_valores)

        nova_cartela = preecher_cartela(cartela, num_sorteado)
        
        # printa a tabela a cada número sorteado
        if cartelas_verbose:
            print('\n')
            printar_cartela(nova_cartela)
        
        # para ao vencer e retorna i vezes que levou para isso
        if parar_ao_vencer:
            if verificar_vitoria(nova_cartela):
                return i
    
    return verificar_vitoria(nova_cartela)



### PASSO 1 ###

print('\n########################## PASSO 1 ##########################\n')
cartela1 = criar_cartela()
printar_cartela(cartela1)



### PASSO 2 ###

print('\n########################## PASSO 2 ##########################\n')
# TO DO --> Separar verificação e alteração da tabela



### PASSO 3 ###

print('\n########################## PASSO 3 ##########################\n')
cartela3 = criar_cartela()
printar_cartela(cartela3)

if jogar_bingo(cartela3, qtd_numeros=50, parar_ao_vencer=False, cartelas_verbose=True):
    print('\nA cartela é vencedora!\n')
else:
    print('\nA cartela NÃO é vencedora!\n')

    
    
### PASSO 4 ###

print('\n########################## PASSO 4 ##########################\n')
lista_qtd_necessaria_vitoria = []
cartela4 = criar_cartela()
for _ in range(1000):
    lista_qtd_necessaria_vitoria.append(jogar_bingo(cartela4.copy(), parar_ao_vencer=True))
    
print(f'''
    * O número mínimo de sorteio para que a carteja seja vencedora: {min(lista_qtd_necessaria_vitoria)}
    * A média do número de sorteios para que a carteja seja vencedora: {sum(lista_qtd_necessaria_vitoria)/len(lista_qtd_necessaria_vitoria)}
    * O número máximo de sorteios para que a cartela seja vencedora: {max(lista_qtd_necessaria_vitoria)} ''')