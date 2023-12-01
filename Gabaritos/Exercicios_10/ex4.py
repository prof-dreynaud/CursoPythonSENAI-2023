class Despesa:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

despesasEster = []
total_gasto = 0

while True:
    nome_despesa = input("Digite o nome da despesa ou sair para encerrar: ")

    if nome_despesa.lower() == 'sair':
        break

    valor_despesa = float(input("Digite o valor da despesa: "))

    despesa = Despesa(nome_despesa, valor_despesa)
    despesasEster.append(despesa)
    #total_gasto = total_gasto + valor_despesa
    total_gasto += valor_despesa


print("\nLista de despesas da Ester: ")
for i in despesasEster:
    print(f"{i.nome}: R$ {i.valor: .2f}")

print(f"\nTotal gasto: R$ {total_gasto: .2f}")