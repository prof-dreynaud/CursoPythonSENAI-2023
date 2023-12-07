#Exercício 5

# Crie um programa em Python para simular um sistema bancário simples. 
# Implemente uma classe ContaBancaria que tem os seguintes 

# métodos:

# __init__(self, titular, saldo_inicial): Inicializa a conta bancária com um titular e um saldo inicial.
# deposito(self, valor): Realiza um depósito na conta.
# saque(self, valor): Realiza um saque na conta.
# obter_saldo(self): Retorna o saldo atual da conta.

class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial

    def deposito(self, valor):
        self.saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente. Saque não realizado.")

    def obter_saldo(self):
        return self.saldo

# Exemplo de uso
titular_conta = input("Digite o nome do titular da conta: ")
saldo_inicial = float(input("Digite o saldo inicial da conta: "))

conta = ContaBancaria(titular_conta, saldo_inicial)

# conta.deposito(100.0)
# conta.saque(50.0)

# Menu
while True:
    print("\nEscolha uma operação:")
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Encerrar")

    escolha = input("Digite o número da operação desejada: ")

    if escolha == '1':
        valor_deposito = float(input("Digite o valor do depósito: "))
        conta.deposito(valor_deposito)
    elif escolha == '2':
        valor_saque = float(input("Digite o valor do saque: "))
        conta.saque(valor_saque)
    elif escolha == '3':
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")

# Exibir saldo final
saldo_atual = conta.obter_saldo()
print(f"Saldo final da conta: R$ {saldo_atual:.2f}")