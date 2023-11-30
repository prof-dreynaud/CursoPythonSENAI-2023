# Criar um arquivo de texto
nome_arquivo = "exemplo.txt"

# Abre o arquivo em modo de escrita
with open(nome_arquivo, "w") as arquivo:
    # Escreve algo no arquivo (pode ser uma string ou qualquer conteúdo desejado)
    arquivo.write("Olá, este é um arquivo de texto criado via Python!\n")
    arquivo.write("Aqui está outra linha para demonstração.\n")

# Mensagem indicando que o arquivo foi criado com sucesso
print(f"O arquivo '{nome_arquivo}' foi criado com sucesso.")