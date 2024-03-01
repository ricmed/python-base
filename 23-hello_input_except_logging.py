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

import os
import sys
import logging

log_level = os.getenv('LOG_LEVEL', 'DEBUG').upper()
log = logging.Logger('logs.py', log_level)
ch = logging.StreamHandler()
ch.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - l:%(lineno)d - f:%(filename)s %(message)s'
)
ch.setFormatter(fmt)
log.addHandler(ch)

arguments = {
    'lang': None,
    'count': 1,
}

for arg in sys.argv[1:]:
    try:
        key, value = arg.split("=")
    except ValueError as e:
        log.error(
            "Você precisa usar `=`, você passou %s. Tente algo como `--lang=pt-BR`. %s",
            arg,
            str(e)
        )
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
