# Exercício 4: Busca de Palavra
# Crie um programa que peça ao usuário para digitar uma palavra e verifique se essa palavra está no arquivo "texto.txt". Imprima na tela o resultado da busca.

palavra = input("Digite uma palavra para buscar no arquivo: ")

with open("texto.txt", "r") as arquivo:
    conteudo = arquivo.read()
    if palavra in conteudo:
        print(f"A palavra '{palavra}' foi encontrada no arquivo.")
    else:
        print(f"A palavra '{palavra}' não foi encontrada no arquivo.")