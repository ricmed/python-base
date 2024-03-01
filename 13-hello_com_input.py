#!/usr/bin/env python3
""""Hello World Multi Línguas

Dependendo da línguagem configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt-br

Ou informe através do CLI argument '--lang'
Ou usuário terá que digitar

Execução:

    python3 01-hello.py
    ou
    ./01-hello.py
"""
__version__ = "0.1.3"
__author__ = "Ricardo Medeiros"
__license__ = "Unlicense"

import os
import sys

arguments = {
    'lang': None,
    'count': 1,
}

for arg in sys.argv[1:]:
    key, value = arg.split("=")
    key = key.lstrip('-').strip()
    value = value.strip()
    if key not in arguments:
        print(f"Valores inválidos {key}")
        sys.exit()
    arguments[key] = value

current_language = arguments['lang']
if current_language is None:
    if 'LANG' in os.environ:
        current_language = os.getenv('LANG')
    else:
        current_language = input("Qual língua usar?")

current_language = current_language[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "fr_FR": "Bonjour, Monde!",
    "es_ES": "Salut, Mundo!",
}

print(msg[current_language] * int(arguments['count']))
