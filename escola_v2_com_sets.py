#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade

Imprimir a lista de  crianças agrupadas por sala que frequenta cada uma das
atividades.
"""
__version__ = "0.1.1"

sala1 = ["Erick","Maia","Gustavo","Manuel","Sofia","Joana"]
sala2 = ["João", "Antonio", "Carlos", "Maria","Isolda"]

aula_ingles = ["Erick", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erick", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [
        ("Inglês",aula_ingles), 
        ("Música", aula_musica), 
        ("Dança",aula_danca)
        ]
print("#" * 40)

for nome_atividade, atividade in atividades:

    print(f"Alunos da atividade {nome_atividade}\n")
    print("-" * 40)

    # Retornar todos os alunos da sala 1 que tem intersecção com a atividade
    atividade_sala1 = set(sala1) & set(atividade)
    atividade_sala2 = set(sala2) & set(atividade)
    
    print("Sala 1 ", atividade_sala1)
    print("Sala 2 ", atividade_sala2)
    print()
    print("#" * 40)