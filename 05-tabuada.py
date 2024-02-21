#!/usr/bin/env python3
"""Imprime a tabuada do 1 ao 10

---Tabuada do 1---
     1 x 1 = 1
     2 x 1 = 2
     3 x 1 = 3
...
##################
---Tabuada do 2---
    2 x 2 = 4
    3 x 2 = 6
...
##################
"""

__version__ = '0.2'
__author__ = 'Ricardo Medeiros'

numeros = list(range(1, 11))

# Utilizando .format e f-string
for n1 in numeros:
    print("{:^18}".format(f"Tabuada do {n1}"))
    for n2 in numeros:
        resultado = n1 * n2
        print("{:-^18}".format(f"{n1} x {n2} = {resultado}"))
    print("#" * 18)
    print()
