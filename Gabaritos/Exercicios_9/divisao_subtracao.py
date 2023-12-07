# Simulando 10 dividido por 2
dividendo = 10
divisor = 2

quociente = 0

while dividendo >= divisor:
    dividendo -= divisor
    quociente += 1

print("Resultado:", quociente)