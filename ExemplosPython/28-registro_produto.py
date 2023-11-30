#Tipo do Registro
class Produto:
    def __init__(self, nome, preço, qtde):
        self.nome = nome
        self.preço = preço
        self.qtde = qtde

#Cadastro
produto1 = Produto ("Camiseta", 29.99, 10)

print(produto1.nome)
print(produto1.preço)
print(produto1.qtde)