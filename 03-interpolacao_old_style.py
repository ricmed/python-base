email_tmpl = """
Olá, %(nome)s
Tem interesse em comprar %(produto)s?
Este produto ótimo para resolver %(texto)s
Clique agora em %(link)s
Apenas %(quantidade)d disponíveis!
Preço promocional %(preco).2f
"""

clientes = ["Fernando", "Guilherme", "Marcus"]

for cliente in clientes:
    print(email_tmpl % {
                            "nome": cliente,
                            "produto": "Caneta Stabilo",
                            "texto": "problema de escrita fluída",
                            "link": "http://caneta.com.br",
                            "quantidade": 2,
                            "preco": 2.5
                        }
    )