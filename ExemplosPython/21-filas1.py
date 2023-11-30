class Fila:
    def __init__(self):
        self.items = []

    def esta_vazia(self):
        return len(self.items) == 0

    def tamanho(self):
        return len(self.items)

    def enfileirar(self, item):
        self.items.append(item)

    def desenfileirar(self):
        if self.esta_vazia():
            return None
        return self.items.pop(0)

# Exemplo de uso da fila personalizada
fila = Fila()

fila.enfileirar("A")
fila.enfileirar("B")
fila.enfileirar("C")

tamanho = fila.tamanho()
print("Tamanho da fila:", tamanho)

item = fila.desenfileirar()
print("Item removido:", item)

vazia = fila.esta_vazia()
print("A fila está vazia?", vazia)
