'''Desafio 2:

1. Implemente um jogo em que o usuário tenha que adivinhar o somatório de dois dados.
O jogo deve sortear um número para cada dado. Estes números devem variar entre 1 e 6, inclusive. 
Deve-se calcular a soma dos dois valores.

2. O usuário deve informar um número. O número informado pelo usuário deve ser validado: 
não pode ser inferior a 2 ou superior a 12. Enquanto o usuário informar um número inválido, 
o jogo deve solicitar a entrada de um novo número.

3. O número do usuário deve ser analisado e o resultado da jogada deve ser apresentado na tela:
    - Caso o usuário informe um número superior ou inferior à soma dos dados, 
    o jogo deve apresentar a mensagem “Você errou. A soma dos dados é x. 
    O valor do primeiro dado é d1 e o do segundo é d2. ”, sendo x o valor da soma, 
    d1 o valor do primeiro dado e d2 o valor do segundo dado.
    - Caso o usuário informe um número igual ao valor da soma, 
    o jogo deve apresentar a mensagem “Parabéns! Você acertou a soma dos dados! 
    O valor do primeiro dado é d1 e o do segundo é d2. ”, 
    sendo d1 o valor do primeiro dado e d2 o valor do segundo dado

4. Ao final do jogo, deve-se questionar o usuário se ele deseja jogar novamente. 
Caso afirmativo, todo o processo deve ser repetido. Caso contrário, o jogo deve ser encerrado.'''


from random import randint
from time import sleep


def jogo_dados(num_dados=2):
    ''' Função sorteia n dados (entre 1 e 10) e o usuário tenta adivinhar'''
    
    if num_dados not in range(1,11):
        print('O jogo só aceita de 1 a 10 dados!!!\n')
        
        return None

    lista_ordinais = ['primeiro', 'segundo', 'terceiro', 'quarto', 'quinto',
    'sexto', 'sétimo', 'oitavo', 'nono', 'décimo']

    dados = [randint(1,6) for _ in range(num_dados)]
    
    while True: 
        #print(dados)

        chute_usuario = input(f'Chute um número entre {num_dados} e {num_dados*6}: ')
        sleep(0.5)

        # O usuario digitou um numero?
        if not chute_usuario.isdigit():
            print(f'\nVocê precisa digitar um NÚMERO entre {num_dados} e {num_dados*6}!\n')
            continue

        chute_usuario = int(chute_usuario)

        # O número digitado está entre num_dados e num_dados * 6 ?
        if chute_usuario not in range(num_dados,(num_dados*6)+1):
            print(f'\nO NÚMERO DIGITADO NÃO ESTÁ ENTRE {num_dados} e {num_dados*6}!\n')
            continue

        # Vitoria ou derrota
        if chute_usuario == sum(dados):
            texto_inicial = '\nParabéns! Você acertou a soma dos dados!\n'
        else:
            texto_inicial = f'\nVocê errou :(\nA soma dos dados era igual a {sum(dados)}.\n'

        # Criando o texto final
        sleep(1)
        texto_final = ''
        for i in range(num_dados):
            texto_final += f'\tO valor do {lista_ordinais[i]} dado era {dados[i]}.\n'

        print(texto_inicial + texto_final)

        sleep(1)

        return None


# codigo
while True:
    jogo_dados(num_dados=2)
    print('\nVocê deseja jogar novamente? ')
    sleep(1)
    continuar =  input('Digite QUALQUER CARACTERE para SIM ( ou Pressione ENTER para NÃO ) --> ')

    if not continuar:
        break

print('\nObrigado por jogar!')