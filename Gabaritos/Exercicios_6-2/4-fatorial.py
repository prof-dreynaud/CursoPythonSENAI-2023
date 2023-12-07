def fatorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * fatorial(numero - 1)

numero = int(input("Digite um número inteiro: "))
resultado = fatorial(numero)
print("O fatorial de", numero, "é", resultado)