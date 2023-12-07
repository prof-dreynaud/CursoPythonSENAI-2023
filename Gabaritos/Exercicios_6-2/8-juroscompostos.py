principal = float(input("Digite o principal (montante inicial): "))
taxa_juros = float(input("Digite a taxa de juros anual (%): "))
tempo = int(input("Digite o período de tempo (anos): "))

montante = principal * (1 + taxa_juros / 100) ** tempo
print("O montante final é:", montante)