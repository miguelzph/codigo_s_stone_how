"""
How Bootcamps - Stone - /código[s]
Data: 31/03/2022
Autor: Henrique Junqueira Branco
Enunciado: Construa um jogo da forca!
A palavra secreta é representada por uma linha de traços em cada letra da palavra. 
Esta pode vir de uma variável ou arquivo, como achar melhor.
Se o jogador que adivinha sugerir uma letra que ocorre na palavra, o programa a escreve em todas as posições corretas. 
Se a letra sugerida for incorreta, o programa deve mostrar isso de alguma forma (desenho, mensagem, etc.).
As tentativas (acertos e erros) são definidas em variáveis.
Quando se esgotarem as tentativas, o programa finaliza dizendo que o jogador perdeu e mostra a palavra correta.
Algumas funções, importações e variáveis foram pré-definidas para auxiliá-los!
"""

from utils import WORDS, STATUS

from random import choice


def get_secret_word(list_of_words):
    """Devolve uma palavra aleatória de uma lista."""
    
    return choice(list_of_words).lower()


def print_game_board(secret_word: str, correct_letters: str, attemps: int, error: int, status: list) -> None:
    """Imprime a situação atual do jogo."""
    
    # substitui por '_' as letras que ainda não foram acertadas
    word_current_state = ''.join(['-' if s_letter not in correct_letters else s_letter for s_letter in secret_word])
    
    print(status[error])
    
    print(f'\nVocê ainda têm {attemps - error} tentativas!')
    print(f'A palavra é: {word_current_state}\n')
    
    return None


def read_input_player(already_typed_letters: list) -> str:
    """Lê uma letra do usuário."""
    letter = input('Digite uma letra: ')
    
    # verifica tamanho e tipo
    if len(letter) != 1 or not letter.isalpha():
        print('Você deve digitar apenas uma letra do alfabeto!\n')
        return read_input_player(already_typed_letters)
    
    # verifica se a letra já foi digitada
    if letter in (already_typed_letters):
        print('A letra já foi digitada!\n')
        print(f'As seguintes letras já foram digitadas: {" ".join(sorted(already_typed_letters))}\n\n')
        return read_input_player(already_typed_letters)
         
    return letter.lower()


def guess_letter(letter: str, secret_word: str, correct_letters: list, missed_letters: list) -> bool:
    """Verifica se uma letra está na palavra secreta ou já foi jogada, seja certa ou errada."""
      
    # verifica se a letra está ou não na palavra
    if letter in secret_word:
        print('Letra correta!')
        correct_letters.append(letter)
        return True
    else:
        print('Letra incorreta!')
        missed_letters.append(letter)
        return False

    
def verify_victory(secret_word: str, correct_letters: str) -> bool:
    '''Verifica se o jogador venceu o jogo'''
    letters_secret_word = [letter for letter in secret_word]
    
    if set(letters_secret_word) == set(correct_letters):
        return True
    else:
        return False


def game_continue(secret_word: str, correct_letters: str, error: int, attemp: int, status: list) -> bool:
    """Função que decide se jogo já encerrou ou não."""
    
    # verifica vitoria
    if verify_victory(secret_word, correct_letters):
        print(f'\nParabéns! Você acertou a palavra "{secret_word}"!\n')
        return False
    else: 
        # quantidade de erros
        if error < attemp:
            return True
        else:
            print(status[-1])
            print(f'\nInfelizmente você não acertou! A palavra era "{secret_word}"!\n')
            return False


secret_word = get_secret_word(WORDS)
correct_letters = []  # variável que armazena as letras corretas já jogadas
missed_letters = []  # variável que armazena as letras incorretas já jogadas
error = 0  # erro inicial
attempts = 6  # tentativas

print(secret_word)

print('Bem vindo!\n')

while game_continue(secret_word, correct_letters, error, attempts, STATUS):
    
    
    print_game_board(secret_word, correct_letters, attempts, error, STATUS)
    
    letter = read_input_player(correct_letters + missed_letters)
    
    if not guess_letter(letter, secret_word, correct_letters, missed_letters):       
        error += 1

