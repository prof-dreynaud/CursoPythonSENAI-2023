# Exercício 4

# Crie um programa em Python que ajude o usuário a controlar suas despesas. 
# O programa deve solicitar ao usuário que insira o nome da despesa e o valor. 
# Em seguida, exiba a lista de despesas e o total gasto.

class Despesa:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

despesas = []
total_gasto = 0

while True:
    nome_despesa = input("Digite o nome da despesa (ou 'sair' para encerrar): ")
    
    if nome_despesa.lower() == 'sair':
        break
    
    valor_despesa = float(input("Digite o valor da despesa: "))
    
    despesa = Despesa(nome_despesa, valor_despesa)
    despesas.append(despesa)
    total_gasto += valor_despesa

print("\nLista de despesas:")
for despesa in despesas:
    print(f"{despesa.nome}: R$ {despesa.valor:.2f}")

print(f"\nTotal gasto: R$ {total_gasto:.2f}")