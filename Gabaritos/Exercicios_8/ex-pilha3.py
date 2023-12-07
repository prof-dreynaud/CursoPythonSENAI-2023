#Exercício 3:
#Enunciado: Crie uma função que recebe uma pilha e retorna o elemento no topo da pilha sem removê-lo.

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

def elemento_no_topo(pilha):
    if not pilha.is_empty():
        return pilha.items[-1]
    return None

pilha = Pilha()
pilha.push(1)
pilha.push(2)
pilha.push(3)
pilha.push(10)
resultado = elemento_no_topo(pilha)
print(resultado)  # Deve imprimir 10