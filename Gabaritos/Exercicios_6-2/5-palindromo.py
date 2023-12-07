palavra = input("Digite uma palavra: ").lower()
reverso = palavra[::-1]

if palavra == reverso:
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")