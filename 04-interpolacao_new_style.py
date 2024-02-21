#!/usr/bin/env python3

# Utilizando str.format
msg = 'Olá, {nome} você é o player {posicao:03d} e você possui {pontos:.3f} pontos'

print(msg.format(nome="Ricardo", posicao=3, pontos=892.87))


# Utilizando f-string
nome = 'Ricardo'
saldo = 1230.59
print(f"{nome}, você possui R${saldo:.2f} de saldo")

# Existem várias formas de alinhar um texto, usando ^, >, <
nome = 'Ricardo'
print(f"{nome:^20}")
print(f"{nome:-^20}")
print(f"{nome:->20}")
print(f"{nome:-^20.3}")

'''
Para a biblioteca logging deve-se usar a concatenação com %s, pois esta é uma biblioteca
muito antiga

Para mensagens longas usamos o str.format{}

f-strings para o restante (mensagens curtas, erros, etc)
'''

# Imprimir emoji
print("\U0001F43C")  # Código Unicode do emoji
print("\N{panda face}")  # Nome do emoji
