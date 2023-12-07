#Exercício 3: Contagem de Linhas
#Crie um programa que conte e imprima na tela o número de linhas do arquivo "texto.txt".

with open("texto.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    numero_de_linhas = len(linhas)
    print(f"O arquivo possui {numero_de_linhas} linhas.")