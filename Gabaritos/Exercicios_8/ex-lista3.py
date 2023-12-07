#Exercício 3:
#Enunciado: Crie uma função que receba uma lista de números inteiros e retorne a média dos valores na lista.

def calcular_media(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

numeros = [10, 20, 30, 40, 50]
resultado = calcular_media(numeros)
print(resultado)  # Deve imprimir 30.0