'''Desafio 1:

Implemente um jogo em que o usuário tenha que adivinhar um número sorteado pelo computador.

1. O jogo deve sortear um número entre 1 e 100.
2. O usuário deve informar um número. O número informado pelo usuário deve ser validado: não pode ser inferior a 1 ou superior a 100. Enquanto o usuário informar um número inválido, o jogo deve solicitar a entrada de um novo número.
3. O número do usuário deve ser analisado:
    - Caso o usuário informe um número inferior ao número sorteado, o jogo deve apresentar a mensagem “O número sorteado é maior.”.
    - Caso o usuário informe um número superior ao número sorteado, o jogo deve apresentar a mensagem “O número sorteado é menor.”.
    - Caso o usuário informe um número igual ao número sorteado, o jogo deve apresentar a mensagem “Parabéns! Você acertou o número sorteado” e o jogo deve ser finalizado, sendo apresentado ao usuário a quantidade de tentativas efetuadas até este momento.
4. Ao final do jogo, deve-se questionar o usuário se ele deseja jogar novamente. Caso afirmativo, todo o processo deve ser repetido. Caso contrário, o jogo deve ser encerrado.
'''


from random import randint
from time import sleep


# criando a funcao do jogo
def jogo_adivinhar_numero():
       
    tentativas = 0
    num_sorteado = randint(1,100)

    print(num_sorteado) # --> para ver o número sorteado

    while True:
        num_jogador = input('Digite um número entre 1 e 100: ')
        sleep(0.5)
        
        # O usuario digitou um numero?
        if not num_jogador.isdigit():
            print('\nVocê precisa digitar um NÚMERO entre 1 e 100!\n')
            continue
   
        num_jogador = int(num_jogador)
    
        # O número digitado está entre 1 e 100 ?
        if num_jogador not in range(1,101):
            print('\nO NÚMERO DIGITADO NÃO ESTÁ ENTRE 1 E 100!\n')
            continue
            
        else:
            tentativas += 1

            if num_jogador < num_sorteado:
                print('\nO número sorteado é maior.')
            elif num_jogador > num_sorteado:
                print('\nO número sorteado é menor.')
            else:
                print(f'\nParabéns! Você acertou o número sorteado com {tentativas} tentativas')
                sleep(1)
                break
                
    return None


# codigo
while True:
    jogo_adivinhar_numero()
    print('\n\nVocê deseja jogar novamente? ')
    sleep(1)
    continuar =  input('Digite QUALQUER CARACTERE para SIM ( ou Pressione ENTER para NÃO ) --> ')
    
    if not continuar:
        break
        
print('\nObrigado por jogar!')