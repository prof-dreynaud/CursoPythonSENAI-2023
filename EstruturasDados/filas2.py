import queue

#Criar fila vazia
fila = queue.Queue()

fila.put("A")
fila.put("B")
fila.put("C")
fila.put("D")

#tamanho??
tamanho = fila.qsize()
print("Tamanho da fila: ", tamanho)

#remover
item = fila.get()
print("item removido: ", item)

#será que removeu?
tamanho = fila.qsize()
print("Tamanho da fila: ", tamanho)

#verificar se a fila está vazia
vazia = fila.empty()
print("A fila está vazia?? ", vazia)
