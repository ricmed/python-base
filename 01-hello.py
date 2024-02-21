#!/usr/bin/env python3
""""Hello World Multi Linguas

Dependendo da líguo configurada no ambiente o programa exibe a mensagem 
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt-br

Execução:

    python3 01-hello.py
    ou
    ./01-hello.py
"""
__version__ = "0.0.1"
__author__ = "Ricardo Medeiros"
__license__ = "Unlicense"

# Dunder - indica 2 underlines antes e depois da palavra

import os

current_language = os.getenv("LANG", "en_US")[:5]  # idioma padrão en_US

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "fr_FR":
    msg = "Bonjour, Monde!"

print(msg)
