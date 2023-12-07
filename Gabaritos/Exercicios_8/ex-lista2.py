#Exercício 2:
#Enunciado: Escreva uma função que receba uma lista de palavras e retorne a mesma lista, mas sem palavras repetidas.

def remover_palavras_repetidas(lista):
    return list(set(lista))

palavras = ["apple", "banana", "cherry", "apple", "date", "banana"]
resultado = remover_palavras_repetidas(palavras)
print(resultado)  # Deve imprimir ["apple", "banana", "cherry", "date"]