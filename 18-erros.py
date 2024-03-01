#!/usr/bin/env python3
"""Tratamento de erros
"""

import os
import sys

try:
    names = open("names.txt").readlines()
except FileNotFoundError as e:
    print(f"[Error] {e}")
    sys.exit(1)
else:
    print("Sucesso!")
finally:
    print("Execute isso sempre!")

try:
    print(names[2])
except:
    print ("[Error] Missing name in the list")
    sys.exit(1)