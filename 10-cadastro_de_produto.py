#!/usr/bin/env python3
"""Cadastro de Produto

Uso de dicionários
"""
__version__ = "0.1"
__author__ = 'Ricardo Medeiros'

import pprint  # preaty print

# Implementa hashtable, um misto entre o set e a list
produto = {
    "nome": "Caneta",
    "cores": ["azul", "branco"],
    "preco": 3.23,
    "dimensao": {
        "altura": 12.1,
        "largura":  0.8
    },
    "em_estoque": True,
    "config": 45678,
    "codebar": None,
}

cliente = {
    "cod": 21,
    "nome": "Ricardo"
}

compra = {
    "cliente": cliente,
    "produto": produto,
    "quantidade": 3
}

# pprint.pprint(compra)

total_compra = compra['quantidade'] * compra["produto"]['preco']

print(
    f"O cliente {compra['cliente']['nome']} comprou {compra['produto']['nome']}"
    f" e pagou o total de {total_compra}"
    f" por {compra['quantidade']} unidade(s) "
)







for key in produto:
    print(key, "->", produto[key])
#ou
for key, value in produto.items():
    print(key, "-->", value)






## Combinando 2 dicionários ##
# informacao original
cliente = {"nome": "Bruno", "cidade": "Viana"}

# informacao adicional
extra = {"pais": "Portugal"}

# Informação final
final = {**cliente, **extra}
print(final)


## Fazendo update inplace ##
# informacao original
cliente = {"nome": "Bruno", "cidade": "Viana"}

# informacao adicional
extra = {"pais": "Portugal"}

# Cliente atualizado
cliente.update(extra)
print(cliente)