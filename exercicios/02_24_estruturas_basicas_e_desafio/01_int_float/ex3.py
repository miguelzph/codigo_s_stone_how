# Exercício 3:

# No exercício acima você calculou a área de um triângulo a partir da sua base e altura. 
# Faça um programa que receba os 3 lados de um triângulo – s1, s2 e s3 – e calcule sua área. 
# Compare a resposta com o exercício acima, dada das mesmas entradas. Os resultados devem ser idênticos.


s1 = float(input('Digite o primeiro lado do triângulo: '))
s2 = float(input('Digite o segundo lado do triângulo: '))
s3 = float(input('Digite o terceiro lado do triângulo: '))

s = (s1+s2+s3)/2

area = (s * (s-s1) * (s-s2) * (s-s3)) ** (1/2)

print(f'A área do triângulo é {area:.2f} unidades²')