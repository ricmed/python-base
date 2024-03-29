#!/usr/bin/env python3
"""Calculadora Prefix.

Funcionamento:

[operação] [n1] [n2]

Operações:
sum → +
sub → -
mul → *
div → /

Uso:
$ prefixcalc.py sum 5 2
7

$ prefixcalc.py mul 10 5
50

$ prefixcalc.py
operação: sum
n1: 5
n2: 4
9

Os resultados serão salvos em calc.log
"""

import sys
import os

from datetime import datetime

while True:
    arguments = sys.argv[1:]

    if not arguments:
        operation = input("operação:")
        n1 = input("n1:")
        n2 = input("n2:")
        arguments = [operation, n1, n2]
    elif len(arguments) != 3:
        print("Número de argumentos inválidos")
        print("ex: `sum 5 5`")
        sys.exit(1)

    operation, *nums = arguments

    valid_operations = ("sum", "sub", "mul", 'div')
    if operation not in valid_operations:
        print("Operação inválida")
        print(valid_operations)
        sys.exit(1)

    validated_nums = []
    for num in nums:
        if not num.replace(".", "").isdigit():
            print(f"Numero inválido {num}")
            sys.exit(1)
        if "." in num:
            num = float(num)
        else:
            num = int(num)
        validated_nums.append(num)

    n1, n2 = validated_nums

    if operation == "sum":
        result = n1 + n2
    elif operation == "sub":
        result = n1 - n2
    elif operation == "mul":
        result = n1 * n2
    elif operation == "div":
        result = n1 / n2

    path = os.curdir
    filepath = os.path.join(path, "15-calc.log")
    timestamp = datetime.now().isoformat()
    user = os.getenv("USER", "unknown")

    try:
        with open(filepath, "a") as log:
            log.write(f"{timestamp} - {user} - {operation},{n1},{n2} = {result}\n")
    except PermissionError as e:
        print(str(e))
        sys.exit(1)

    # ou

    # print(f"{operation}, {n1}, {n2} = {result}\n", file=open(filepath, "a"))

    print(f"O resultado é {result}")

    if input("Pressione enter para continar ou qualquer tecla para sair"):
        break
