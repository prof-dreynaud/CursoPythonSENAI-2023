pilha = []

pilha.append(10)
pilha.append(20)
pilha.append(30)
pilha.append(40)
pilha.append(50)

print("Topo da pilha: ", pilha[-1])

elemento_removido = pilha.pop()
print("Elemento removido: ", elemento_removido)

print("Topo da pilha: ", pilha[-1])

if not pilha:
    print ("A pilha está vazia")

else:
    print("ainda tem elementos...") 