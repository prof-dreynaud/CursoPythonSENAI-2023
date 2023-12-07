#Exercício 2:

#Crie uma classe chamada Carro com os seguintes campos: marca, modelo e ano de fabricação.
#Em seguida, crie uma lista de objetos Carro contendo informações de pelo menos três carros diferentes. Percorra a lista e exiba as informações de cada carro.

class Carro:
    def __init__(self, marca, modelo, ano_fabricacao):
        self.marca = marca
        self.modelo = modelo
        self.ano_fabricacao = ano_fabricacao

carro1 = Carro("Ford", "Fiesta", 2018)
carro2 = Carro("Chevrolet", "Onix", 2020)
carro3 = Carro("Volkswagen", "Golf", 2019)

carros = [carro1, carro2, carro3]

for carro in carros:
    print("Marca:", carro.marca)
    print("Modelo:", carro.modelo)
    print("Ano de Fabricação:", carro.ano_fabricacao)
    print()