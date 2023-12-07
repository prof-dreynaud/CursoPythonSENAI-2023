#Exercício 3:

#Crie uma classe chamada Produto com os seguintes campos: código, nome, preço e quantidade em estoque. 
#A classe deve ter um método chamado calcular_total, que retorna o valor total em reais do estoque desse produto (preço multiplicado pela quantidade em estoque). 
#Crie três instâncias dessa classe, atribua valores diferentes aos campos e exiba o valor total em reais do estoque de cada produto.

class Produto:
    def __init__(self, código, nome, preço, quantidade):
        self.código = código
        self.nome = nome
        self.preço = preço
        self.quantidade = quantidade

    def calcular_total(self):
        return self.preço * self.quantidade

produto1 = Produto(1, "Camiseta", 29.99, 10)
produto2 = Produto(2, "Calça", 59.99, 5)
produto3 = Produto(3, "Sapato", 99.99, 3)

print("Produto 1 -", produto1.nome)
print("Valor total em estoque:", produto1.calcular_total())
print()

print("Produto 2 -", produto2.nome)
print("Valor total em estoque:", produto2.calcular_total())
print()

print("Produto 3 -", produto3.nome)
print("Valor total em estoque:", produto3.calcular_total())

#Neste exercício, criamos a classe Produto com os campos código, nome, preço e quantidade em estoque. 
# A classe possui um método calcular_total, que multiplica o preço pelo quantidade para obter o valor total em estoque do produto.
#Em seguida, criamos três instâncias da classe Produto com valores diferentes para cada campo. 
# Por fim, utilizamos o método calcular_total para exibir o valor total em reais do estoque de cada produto.