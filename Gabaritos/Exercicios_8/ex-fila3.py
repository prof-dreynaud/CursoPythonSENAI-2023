#Exercício 3:
#Enunciado: Crie uma função que recebe uma fila e retorna o elemento mais antigo da fila sem removê-lo.

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

def elemento_mais_antigo(fila):
    if not fila.is_empty():
        return fila.items[0]
    return None

fila = Fila()
fila.enqueue(1)
fila.enqueue(2)
fila.enqueue(3)
resultado = elemento_mais_antigo(fila)
print(resultado)  # Deve imprimir 1
