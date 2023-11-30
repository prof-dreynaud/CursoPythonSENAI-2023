#Abre e fecha automaticamente o arquivo
with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)