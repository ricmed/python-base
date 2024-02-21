#!/usr/bin/env python3
"""
Imprime a tabuada do 1 ao 10
"""

__version__ = '0.1'
__author__ = 'Ricardo Medeiros'

numeros = list(range(1, 11))

for n1 in numeros:
    print("Tabuada do:", n1)
    for n2 in numeros:
        print(n1 * n2)
    print('#' * 18)
