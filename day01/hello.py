#!/usr/bin/env python3
"""Primeiro programa em Python

# para dar permissão de execução ao arquivo
chmod +x 01-hello.py

Hello Word Multi Línguas

Dependendo da língua configurada n ambiente o programa exibe a mensagem 
correspondente

Como usar:
Tenha a variável LANG devidamente configurada
    export LANG=pt_BR

Execução:
    python3 01-hello.py
    ou
    ./01-hello.py
"""
__version__ = "0.1"
__author__ = "Ricardo Medeiros"
__license__ = "Unlicense"

# Dunder = __ (underline, underline)

import os

current_language = os.getenv('LANG', 'en_US')[:5]

msg = 'Hello, World!'

if current_language == 'pt_BR':
    msg = 'Olá, Mundo!'
elif current_language == 'it_IT':
    msg = 'Ciao, Mondo!'

print(msg)