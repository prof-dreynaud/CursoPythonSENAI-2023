#adição de texto no arquivo
arquivo = open("dados.txt","a")

#escrever dados no arquivo
arquivo.write("\nOla mundo SENAI!")
arquivo.write("\nDisciplina Estrutura de Dados")

#fechar arquivo
arquivo.close()