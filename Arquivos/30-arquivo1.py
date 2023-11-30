#abrir arquivo
arquivo = open("dados.txt","r")

#ler o conteúdo
conteudo = arquivo.read()

#fechar o arquivo
arquivo.close()

#exibir no terminal
print(conteudo)