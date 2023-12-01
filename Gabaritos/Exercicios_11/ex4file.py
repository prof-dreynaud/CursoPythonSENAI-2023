palavra = input("Digite uma palavra para buscar no arquivo: ")

with open("texto.txt", "r") as arquivo:
    conteudo = arquivo.read()

    if palavra in conteudo:
        print(f"A palavra '{palavra}' foi encontrada no texto!")

    else:
        print(f"A palavra '{palavra}' não foi encontrada no texto!")