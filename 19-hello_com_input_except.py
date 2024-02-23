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
    try:
        key, value = arg.split("=")
    except ValueError as e:
        # TODO Logging
        print(f"[ERRO] {str(e)}")
        print(f"Argumento inválido {arg}, você precisa usar `=`")
        print(f"Você passou {arg}")
        print("Tente algo como `--lang=pt-BR`")
        sys.exit(1)
    key = key.lstrip('-').strip()
    value = value.strip()

    # validando se a chave existe
    if key not in arguments:
        print(f"Valores inválidos {key}")
        sys.exit()
    arguments[key] = value

current_language = arguments['lang']

if current_language is None:
    # TODO: Usar repetição
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
try:
    mensagem = msg[current_language]
except KeyError as e:
    print(f"[ERRO] {str(e)}")
    print(f"Língua inválida {current_language}")
    print(f"Líguas disponívels: {msg.keys()}")
    sys.exit(1)

print(msg[current_language] * int(arguments['count']))
