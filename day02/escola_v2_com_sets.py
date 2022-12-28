#!/usr/bin/env python3

"""Exibe relatório de alunos por atividade.
Imprimir a lista de alunos agrupados por sala que frequenta cada 
uma das atividades 
"""
__version__ = '0.1'

sala1 = ['Erik', 'Maia', 'Gustavo', 'Manuel', 'Sofia','Joana']
sala2 = ['João', 'Antonio', 'Carlos', 'Maria', 'Isolda']

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [
    ('Inglês',aula_ingles),
    ('Música', aula_musica),
    ('Dança', aula_danca)]

# Listar alunos em cada atividade por sala

for nome_atividade, atividade in atividades:

    print(f'Alunos da atividade {nome_atividade}\n')
    print('*' * 40)

    # sala1 que tem interseção com a atividade
    # faz interseção de 2 formas
    atividade_sala1 = set(sala1) & set(atividade)
    atividade_sala2 = set(sala2).intersection(atividade)

    print(f'A sala 1', atividade_sala1)
    print(f'A sala 2', atividade_sala2)
    print()
    print('#' * 40)