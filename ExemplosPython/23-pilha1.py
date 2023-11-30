pilha = []

pilha.append(10)
pilha.append(20)
pilha.append(30)

print("Topo da pilha:", pilha[-1])

elemento_removido = pilha.pop()
print("Elemento removido:", elemento_removido)

if not pilha:
    print("A pilha está vazia.")

else:
    print("Ainda tem elementos!")