#Uso funções def

def calcular_soma(a, b):
    return a + b

def calcular_subtracao(a, b):
    return a - b

def calcular_multiplicacao(a, b):
    return a * b

def calcular_divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"

#variáveis
a = 10
b = 5

soma = calcular_soma(a, b)
subtracao = calcular_subtracao(a, b)
multiplicacao = calcular_multiplicacao(a, b)
divisao = calcular_divisao(a, b)

print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)