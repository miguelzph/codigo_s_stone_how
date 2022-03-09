'''Exercício 4:

Faça um programa que receba a temperatura média de cada mês do ano e 
armazene-as em uma lista. Em seguida, calcule a média anual das temperaturas e
mostre a média calculada juntamente com todas as temperaturas acima da média anual, 
e em que mês elas ocorreram (mostrar o mês por extenso: Exemplo de saída:
>>> Meses com temperatura acima da média anual de 35,5°:
>>> 1 – janeiro
>>> 3 – março
>>> 6 – junho'''

lista_meses = [
    '1 - janeiro', '2 - fevereiro', '3 - março', '4 - abril', '5 - maio', '6 - junho', 
    '7 - julho','8 - agosto', '9 - setembro', '10 - outubro', '11 - novembro', '12 - dezembro'
]

lista_temps = [25.4, 27.6, 25.6, 34.7, 27.4, 33.2, 33.6, 26.2, 29.4, 36.9, 22.9, 26.5]

# nao consegui fazer sem for
meses_maior_media = [mes for (mes, temperatura) in zip(lista_meses, lista_temps) if temperatura > media_temp]

media_temp = round(sum(lista_temps) / len(lista_temps), 1)
print(f'Meses com temperatura acima da média anual de {media_temp}°:')
print('\n'.join(meses_maior_media))