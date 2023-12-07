# Simulando 2 elevado a 8 usando apenas adição
base = 2
expoente = 8

resultado = 1  # Inicializando com 1, pois qualquer número elevado a 0 é 1

for _ in range(expoente):
    temp_resultado = 0
    for _ in range(base):
        temp_resultado += resultado
    resultado = temp_resultado

print("Resultado:", resultado)