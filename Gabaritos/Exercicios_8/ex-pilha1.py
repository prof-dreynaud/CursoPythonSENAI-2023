#Exercício 1:
#Enunciado: Implemente uma pilha usando uma lista em Python. Crie funções push para adicionar um elemento e pop para remover o elemento no topo da pilha.

class Pilha:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

pilha = Pilha()
pilha.push(1)
pilha.push(2)
pilha.push(3)
print(pilha.pop())  # Deve imprimir 3