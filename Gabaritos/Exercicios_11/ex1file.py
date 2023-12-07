#Exercício 1: Leitura de Arquivo
#Crie um programa que abra o arquivo "texto.txt", leia o seu conteúdo e imprima na tela.

with open("texto.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)