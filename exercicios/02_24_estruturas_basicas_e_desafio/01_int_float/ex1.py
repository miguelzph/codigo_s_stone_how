# Exercício 1:

# Faça um programa que receba dois números inteiros do usuário, A e B e imprima na tela as seguintes operações:
# A soma de A e B;
# A diferença quando se subtrai B de A;
# O produto (multiplicação) entre A e B;
# O quociente (parte inteira da divisão) quando se divide A por B;
# O resto da divisão entre A e B;
# O resultado de log10 de A;
# O resultado de A elevado a B;


from math import log10

num_a = int(input('Digite o primeiro número: '))
num_b = int(input('Digite o segundo número: '))

print(f'\n\nA soma de A e B é: {num_a + num_b}')
print(f'A diferença quando se subtrai B de A é: {num_a - num_b}')
print(f'O produto (multiplicação) entre A e B é: {num_a * num_b}')
print(f'O quociente (parte inteira da divisão) quando se divide A por B é: {num_a // num_b}')
print(f'O resto da divisão entre A e B é: {num_a % num_b}')
print(f'O resultado de log10 de A é: {log10(num_a)}')
print(f'O resultado de A elevado a B é: {num_a ** num_b}')
