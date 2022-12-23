# Utilizando interpolação

email_tmpl = """
   Olá, %(nome)s
   Tem interesse em compra %(produto)s?
   Este destino é ótimo para %(texto)s.
   Clique agora em %(link)s
   Apenas %(quantidade)d disponíveis!
   Preço promocional de %(preco).2f
   """

clientes = ['Marcos', 'Alcinês','David', 'Fernado']

for cliente in clientes:
    print(email_tmpl % {'nome': cliente, 
                        'produto':'viagem para Paracuru',
                        'link': 'viagem.com.br',
                        'quantidade': 1, 
                        'preco': 1499, 
                        'texto': 'descansar'})
