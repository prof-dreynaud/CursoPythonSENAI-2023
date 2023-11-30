nomes = ["Alice", "Bob", "Carol", "David"]

# Percorrendo a lista e exibindo os nomes
for nome in nomes:
    print(nome)

# Verificando se um nome está na lista
if "Bob" in nomes:
    print("Bob está na lista")

# Concatenando duas listas
outros_nomes = ["Eve", "Frank"]
todos_nomes = nomes + outros_nomes
print(todos_nomes)  # Saída: ["Alice", "Bob", "Carol", "David", "Eve", "Frank"]
