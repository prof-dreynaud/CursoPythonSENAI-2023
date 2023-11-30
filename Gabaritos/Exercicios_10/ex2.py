#Ex2 Registros

class Carro:
    def __init__(self, marca, modelo, ano_fab):
        self.marca = marca
        self.modelo = modelo
        self.ano_fab = ano_fab

carro1 = Carro("VW", "Fusca", 1976)
carro2 = Carro("Fiat", "Uno", 1986)
carro3 = Carro("Ford", "Fiesta", 2000)

lista = [carro1, carro2, carro3]

for cont in lista:
    print("Marca:", cont.marca)
    print("Modelo:", cont.modelo)
    print("Ano:", cont.ano_fab)
    print()


    