n = int(input("Digite o valor de N para gerar a sequência Fibonacci: "))
a, b = 0, 1
while a <= n:
    print(a, end=" ")
    a, b = b, a + b