"""
How Bootcamps - Stone - /código[s]
Autor: Henrique Junqueira Branco
Enunciado:
Quadrado mágico: Um quadrado mágico é aquele dividido em linhas e colunas, 
com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. 
Por exemplo, veja um quadrado mágico de lado 4, com números de 1 a 16:
01  05  09  16
06  07  02  10
08  03  04  11
12  15  14  13
Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. 
Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. 
Usar um vetor (lista) de 1 a 16 parece ser mais simples que usar uma matriz 4x4.
Extra: Permita que o usuário indique o tamanho do cubo mágico (2x2, 3x3, 4x4, etc.)
"""


from itertools import permutations


def read_input_player() -> int:
    """Lê o tamanho do quadrado."""
    num_side = input('\nDigite o tamanho do lado do quadrado: ')
    
    # verifica tamanho e tipo
    if not num_side.isnumeric():
        print('Você deve digitar um número inteiro!\n')
        return read_input_player()
         
    return int(num_side)


def create_all_squares(num_side: int = 3) -> object:
    '''Cria todos os quadrados possíveis 
    
    num_side: número de lados do quadrado
    
    retorna: um objeto do tipo itertools.permutations'''
    
    possible_numbers = range(1, num_side**2 + 1)
    all_squares = permutations(possible_numbers)
    
    return all_squares


def verify_a_square(square: tuple or list, side_number: int) -> bool:
    '''Verifica se um quadrado é mágico ou não
    
    square: quadrado em formato de lista ou tupla
    side_number: tamanho do lado do quadrado
    
    retorna: True é mágico, ou False não é mágico'''
     
    first_diagonal = square[0:len(square):side_number+1]
    
    second_diagonal = square[side_number-1:len(square)-1:side_number-1]
    
    # testing diagonals
    if sum(first_diagonal) != sum(second_diagonal):
        return False
    else:
        sum_diagonal = sum(first_diagonal)
    
    # testing lines and cols
    for side in range(0,side_number):

        col = square[side:side_number**2:side_number]

        line = square[side*side_number:side*side_number + side_number]

        if sum(line) != sum_diagonal or sum(col) != sum_diagonal:
            return False
    return True    

#### Ao alterar o tipo perdi a posição e não dá para seguir mais essa logica
# def find_all_magic_squares(side_number:int) -> list:
    
#     magic_squares = []
    
#     # todas as possibilidades de quadrados
#     all_squares = create_all_squares(side_number)
    
#     # achei uma logica de simetria, então só percorre até a metade
#     for i, square in enumerate(all_squares[:int(len(tuple(all_squares))/2)]):
#         if verify_a_square(square, 3):

#             # quadrado avaliado
#             magic_squares.append(square)

#             # simetrico -> tamanho - i -1
#             magic_squares.append(all_squares[len(all_squares)-i-1])
#     return magic_squares

def find_all_magic_squares(side_number:int) -> list:
    
    magic_squares = []
    i = 0
    
    # todas as possibilidades de quadrados
    all_squares = create_all_squares(side_number)
    
    # percorrendo os quadrados
    for square in all_squares:
        i += 1
        if i % 10000000 ==0:
            print(f'{i/1000000} milhoes')
        if verify_a_square(square, side_number):

            # quadrado avaliado
            magic_squares.append(square)
                   
    return magic_squares


def print_square(square:tuple or list, side_number:None or int = None) -> None:
    
    if side_number is None:
        side_number = int(len(square) ** (1/2))
    
    for side in range(0, side_number):
        line = square[side*side_number:side*side_number + side_number]
        print(' '.join([str(s).rjust(2, '0') for s in line]))
              
    return None


#### 

side_square = read_input_player()

magic_squares = find_all_magic_squares(side_square)

if magic_squares:
    print(f'\nHá {len(magic_squares)} quadrados mágicos de lado, e a constante é {sum(magic_squares[0][:3])}')
    print('\n==============QUADRADOS ==============')
else:
    print(f'\nNão há quadrados mágicos de lado {side_square}\n\n')

for i, square in enumerate(magic_squares):
    
    print('==============')
    print(f'QUADRADO {i+1}')
    print_square(square)