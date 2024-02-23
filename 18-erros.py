#!/usr/bin/env python3
"""Tratamento de erros
"""
__version__ = "0.1"

import os
import sys

try:
    names = open("names.txt").readlines()
except FileNotFoundError as e:
    print(f"[Error] {e}")
    sys.exit(1)
    # TODO: Usar retry
else:
    print("Sucesso!")
finally:
    print("Execute isso sempre!")

try:
    print(names[2])
except:
    print ("[Error] Missing name in the list")
    sys.exit(1)