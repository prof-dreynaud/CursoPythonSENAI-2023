#Exercício 2
#Crie um programa que peça ao usuário para digitar uma frase e salve essa frase no arquivo "frase.txt".

frase = input("Digite uma frase: ")

with open("frase.txt", "w") as arquivo:
    arquivo.write(frase)