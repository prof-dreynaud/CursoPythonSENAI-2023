#Exercício 1:
#Enunciado: Crie uma função em Python que receba uma lista de números inteiros e retorne a soma de todos os números pares na lista.

def soma_numeros_pares(lista):
    soma = 0
    for numero in lista:
        if numero % 2 == 0:
            soma += numero
    return soma

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
resultado = soma_numeros_pares(lista)
print(resultado)  # Deve imprimir 20