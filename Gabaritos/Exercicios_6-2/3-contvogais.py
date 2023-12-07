texto = input("Digite uma palavra ou frase: ").lower()
vogais = "aeiou"
contador = 0

for letra in texto:
    if letra in vogais:
        contador += 1

print("Número de vogais:", contador)