#!/usr/bin/env python3
""""Hello World Multi Línguas

Dependendo da línguagem configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt-br

Execução:

    python3 01-hello.py
    ou
    ./01-hello.py
"""
__version__ = "0.1.2"
__author__ = "Ricardo Medeiros"
__license__ = "Unlicense"

# Dunder - indica 2 underlines antes e depois da palavra

import os

current_language = os.getenv("LANG", "en_US")[:5]  # idioma padrão en_US

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "fr_FR": "Bonjour, Monde!",
    "es_ES": "Salut, Mundo!"
}

print(msg[current_language])
