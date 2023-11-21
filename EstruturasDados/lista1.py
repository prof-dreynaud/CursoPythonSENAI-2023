#Criando uma lista de alunos
nomes = ["Luan","Gustavo","Ester", "Iago"]

#Percorrer a lista
for nome in nomes:
    print(nome)

#Procurar um nome na lista
if "Vinicius" in nomes:
    print("Aluno está presente!")

else:
    print("Aluno faltou!")

#Concatenar outra lista
outros_nomes = ["Helder", "Aduyar"]
todos_alunos = nomes + outros_nomes

print(todos_alunos)