# Exercício 5: Concatenação de Arquivos
# Crie um programa que abra dois arquivos, "arquivo1.txt" e "arquivo2.txt", leia o conteúdo de ambos e salve em um novo arquivo chamado "concatenado.txt".

with open("arquivo1.txt", "r") as arquivo1, open("arquivo2.txt", "r") as arquivo2:
    conteudo1 = arquivo1.read()
    conteudo2 = arquivo2.read()

    with open("concatenado.txt", "w") as arquivo_concatenado:
        arquivo_concatenado.write(conteudo1 + conteudo2)