# Exercício 4:

# Faça um programa que receba do usuário seu peso em kg e altura em metros e imprima o 
# Índice de Massa Corporal (IMC) do usuário.


peso = float(input('Digite o seu peso em kg: '))
altura = float(input('Digite a sua altura em metros: '))

print(f'O seu IMC é: {peso/(altura**2):.2f}')