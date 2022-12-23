# Utilizando str.format
msg = 'Olá, {nome} você é o player {posicao:03d} e você possui {pontos:.3f} pontos'

print(msg.format(nome="Ricardo",posicao= 3, pontos= 892.87))


# Utilizando f-string
nome = 'Ricardo'
saldo = 1230.59
print(f"{nome}, você possui R${saldo:.2f} de saldo")

# Existem várias formas de formatar um texto
nome = 'Bruno'
print(f"{nome:^20}")
print(f"{nome:-^20}")
print(f"{nome:->20}")

'''
Para a biblioteca logging deve-se usar a concatenação, pois esta é uma biblioteca
muito antigo

Para mensagens longas usamos o str.format{}

f-strings para o restante (mensagens curtas, errros, etc)

'''