#!/usr/bin/env python3
"""Template para envio de email

O script vai receber um arquivo com os emails
    emails.txt

O script vai receber um arquivo com o template
    template.txt
"""
__version__ = "0.2"
__author__ = "Ricardo Medeiros"

import sys
import os

arguments = sys.argv[1:]
if not arguments:
    print("Informe o arquivo de emails")
    sys.exit(1)
filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename)
templatepath = os.path.join(path, templatename)

for line in open(filepath):
    nome, email = line.split(",")

    # TODO: Substituir por envio de email
    print(f"Enviando email para {nome} : {email}")
    print()
    print(
        open(templatepath, encoding="utf-8").read()
        % {
            "nome": nome,
            "produto": "Caneta Stabilo",
            "texto": "problema de escrita fluída",
            "link": "http://caneta.com.br",
            "quantidade": 2,
            "preco": 2.5,
        }
    )
    print("="*50)
