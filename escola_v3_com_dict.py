#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade

Imprimir a lista de  crianças agrupadas por sala que frequenta cada uma das
atividades.
"""
__version__ = "0.1.2"

salas = {
    "sala1": ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"],
    "sala2": ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]
}

atividades = {
        "Inglês": ["Erik", "Maia", "Joana", "Carlos", "Antonio"],
        "Música": ["Erik", "Carlos", "Maria"],
        "Dança" : ["Gustavo", "Sofia", "Joana", "Antonio"]
}

for nome_atividade, atividade in atividades.items():

    print(f"Alunos da atividade {nome_atividade}\n")
    print("-" * 40)

    # sala1 e sala 2 que tem interseção com a atividade
    atividade_sala1 = set(salas["sala1"]) & set(atividade)
    atividade_sala2 = set(salas["sala2"]) & set(atividade)

    print("Sala1 ", atividade_sala1)
    print("Sala2 ", atividade_sala2)

    print()
    print("#" * 40)