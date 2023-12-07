#Exercício 2:
#Enunciado: Escreva uma função que recebe uma pilha e retorna o tamanho da pilha.

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

def tamanho_da_pilha(pilha):
    return len(pilha.items)

pilha = Pilha()
pilha.push(1)
pilha.push(2)
pilha.push(3)
pilha.push(4)
pilha.push(10)
resultado = tamanho_da_pilha(pilha)
print(resultado)  # Deve imprimir 5