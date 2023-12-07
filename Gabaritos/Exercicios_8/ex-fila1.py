#Exercício 1:
#Enunciado: Implemente uma fila usando uma lista em Python. Crie funções enqueue para adicionar um elemento e dequeue para remover o elemento mais antigo da fila.

class Fila:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0

fila = Fila()
fila.enqueue(1)
fila.enqueue(2)
fila.enqueue(3)
print(fila.dequeue())  # Deve imprimir 1