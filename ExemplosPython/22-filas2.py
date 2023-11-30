import queue

# Criação de uma fila vazia
fila = queue.Queue()

# Adicionando elementos à fila
fila.put("A")
fila.put("B")
fila.put("C")

# Obtendo o tamanho da fila
tamanho = fila.qsize()
print("Tamanho da fila:", tamanho)

# Removendo elementos da fila (primeiro a entrar, primeiro a sair)
item = fila.get()
print("Item removido:", item)

# Verificando se a fila está vazia
vazia = fila.empty()
print("A fila está vazia?", vazia)
