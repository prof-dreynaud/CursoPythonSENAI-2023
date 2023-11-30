#Edição de arquivo texto
arquivo = open("dados.txt", "w")

#escrever dados no arquivo
arquivo.write("\nOla, mundo\n")
arquivo.write("Este eh um exemplo de arquivo texto!")

#fechar o arquivo
arquivo.close()