#!/usr/bin/env python3

# Desempacotar

pontos = (9, 5, 10)
x, y, z = pontos  # separa em três variáveis
x, *_ = pontos  # O 5 e o 10 ficam na variável _, que vira uma lista

print(x)
print(y)
print(z)
print(_)

users = ['Ricardo', 'Jose', 'Maria', 'Luiz']
print("Lista de usuários:")
print(users)

print("\nInserindo o usuário Jorge ao final da lista:")
users.append('Jorge')
print(users)

print("\nInserindo a usuária Fernanda na posição 2 da lista:")
users.insert(2, 'Fernanda')
print(users)

print("\nRemovendo o usuário Jose")
users.remove('Jose')
print(users)

print("\nRemovendo o último usuário da lista")
users.pop()
print(users)

print("\nConcatenando listas")
users2 = ['Ana', 'Bruna', 'Carla']
print(users + users2)
print()
users.extend(users2)
print('\nNova lista')
print(users)
