#Tipo do registro
class Animal:
    def __init__(self, nome, espécie, idade):
        self.nome = nome
        self.espécie = espécie
        self.idade = idade

#Efetiva o registro
animal = Animal ("Max", "Cachorro", 5)

print(animal.nome)
print(animal.espécie)
print(animal.idade)