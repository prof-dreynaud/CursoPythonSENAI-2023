#Exercício 2:
#Enunciado: Escreva uma função que recebe uma fila e retorna o tamanho da fila.

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

def tamanho_da_fila(fila):
    return len(fila.items)

fila = Fila()
fila.enqueue(1)
fila.enqueue(2)
fila.enqueue(3)
resultado = tamanho_da_fila(fila)
print(resultado)  # Deve imprimir 3