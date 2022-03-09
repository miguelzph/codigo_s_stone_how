'''Exercício 1:

Digamos que existam 2 cursos de idiomas em uma escola, inglês e francês, e que 
existam alunos matriculados conforme abaixo:

Alunos matriculados em inglês:
João Alves dos Santos
Maria Magalhães
Antônio da Silva Ferreira
José Júnior Jarbas
Henrique da Silva Sauro
Joaquina Ferreira da Silva
Fabiana Aparecida Bianco
Marrone Gutierres
Carlos Magno Farad
Antônio da Silva Júnior Amaral

Alunos matriculados em francês:
João Alves dos Santos
Antônio da Silva Ferreira
Fernanda Abdala Mohamed
Abner Mignon Alib
Alisson Figueiredo
Henrique da Silva Sauro
Maria Magalhães
Marrone Gutierres
Joaquina Ferreira da Silva

Faça um programa que responda as seguintes perguntas:

Quantos alunos estão matriculados na escola, no total?
Quantos e quais estão matriculados APENAS em INGLES?
Quantos e quais estão matriculados APENAS em FRANCES?
Quantos e quais estão matriculados EM AMBOS os cursos?
Quantos alunos estão matriculados somente em francês ou somente em inglês, mas não em ambos os cursos?
'''


alunos_ingles = {'João Alves dos Santos',
'Maria Magalhães',
'Antônio da Silva Ferreira',
'José Júnior Jarbas',
'Henrique da Silva Sauro',
'Joaquina Ferreira da Silva',
'Fabiana Aparecida Bianco',
'Marrone Gutierres',
'Carlos Magno Farad',
'Antônio da Silva Júnior Amaral'
}

alunos_frances = {'João Alves dos Santos',
'Antônio da Silva Ferreira',
'Fernanda Abdala Mohamed',
'Abner Mignon Alib',
'Alisson Figueiredo',
'Henrique da Silva Sauro',
'Maria Magalhães',
'Marrone Gutierres',
'Joaquina Ferreira da Silva'}


total_alunos = len(alunos_ingles.union(alunos_frances)) # poderia usar |
print(f'Quantos alunos estão matriculados na escola, no total?   {total_alunos} alunos')

apenas_ingles = len(alunos_ingles.difference(alunos_frances)) # poderia usar &
print(f'Quantos e quais estão matriculados APENAS em INGLES?   {apenas_ingles} alunos')

apenas_frances = len(alunos_frances.difference(alunos_ingles)) # poderia usar -
print(f'Quantos e quais estão matriculados APENAS em FRANCES?   {apenas_frances} alunos')

ambos_cursos = len(alunos_ingles.intersection(alunos_frances)) # poderia usar -
print(f'Quantos e quais estão matriculados EM AMBOS os cursos?   {ambos_cursos} alunos')

apenas_ingles_frances = len(alunos_ingles.symmetric_difference(alunos_frances)) # poderia usar -
print(f'Quantos alunos estão matriculados somente em francês ou somente em inglês, mas não em ambos os cursos?   {apenas_ingles_frances} alunos')