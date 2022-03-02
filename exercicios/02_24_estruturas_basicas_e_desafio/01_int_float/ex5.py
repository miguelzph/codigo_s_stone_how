# Exercício 5:

# Escreva um programa que leia do usuário um número de 4 dígitos e imprima a soma destes dígitos. 
# Exemplo, se o usuário digitar 3141 seu programa deverá imprimir na tela 3+1+4+1=9.


# precisa ser em formato de sting por causa do 0000 até 0999
numero_digitado = str(input('Por favor digite um número de 4 dígitos: '))

# apenas para facilitar a visualização
n = numero_digitado

soma = int(n[0]) + int(n[1]) + int(n[2]) + int(n[3])

print(f'A soma dos dígitos do número {numero_digitado} é igual a {soma}')