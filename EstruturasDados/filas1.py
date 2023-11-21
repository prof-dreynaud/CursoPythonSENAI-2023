class Fila:

    #definição de uma fila sem tamanho e sem elementos
    def __init__(self):
        self.itens = []

    #tamanho da fila
    def tamanho(self):
        return len(self.itens)

    #definindo função enfileirar
    def enfileirar(self, elemento):
        self.itens.append(elemento)

    #valida vazia
    def esta_vazia(self):
        return len(self.itens) == 0

    #função desenfileirar
    def desenfileirar(self):
        if self.esta_vazia():
            return None
        return self.itens.pop(0) #remoção da fila

