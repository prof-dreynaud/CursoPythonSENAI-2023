class TrocaPneus:
    def __init__(self):
        self.pneu_furado = False
        self.pneu_reserva_em_uso = False

    def trocar_pneu_traseiro_esquerdo(self):
        print("1) Estacionar o veículo em local seguro.")
        print("2) Pegar o macaco, chave de roda e estepe.")
        print("3) Elevar o veículo com o macaco.")
        print("4) Retirar a roda furada com a chave de roda.")
        print("5) Colocar o pneu reserva (estepe) no lugar.")
        print("6) Apertar as porcas com a chave de roda.")
        print("7) Baixar o veículo com o macaco.")
        print("8) Verificar se as porcas estão bem apertadas.")
        print("9) Guardar o pneu furado, o macaco e a chave de roda.")
        print("10) Retomar a viagem.")

    def trocar_pneu_verificando_reserva(self):
        print("1) Estacionar o veículo em local seguro.")
        print("2) Pegar o macaco, chave de roda, estepe e verificar o pneu reserva.")
        
        if not self.pneu_reserva_em_uso:
            print("3) Proceder com os passos 3 a 10 da troca do pneu traseiro esquerdo.")
        else:
            print("3) Chamar assistência ou procurar outro meio de transporte.")

    def verificar_e_trocar_pneu_furado(self):
        print("1) Verificar se há algum pneu furado.")
        
        if self.pneu_furado:
            print("2) Pegar o macaco, chave de roda, estepe e verificar o pneu reserva.")
            
            if not self.pneu_reserva_em_uso:
                print("3) Proceder com os passos 3 a 10 da troca do pneu traseiro esquerdo.")
            else:
                print("3) Chamar assistência ou procurar outro meio de transporte.")
        else:
            print("2) Retomar a viagem.")

# Criar uma instância da classe TrocaPneus
troca_pneus = TrocaPneus()

# Simular a troca do pneu traseiro esquerdo
print("### Trocar Pneu Traseiro Esquerdo ###")
troca_pneus.trocar_pneu_traseiro_esquerdo()

# Simular a troca do pneu traseiro esquerdo verificando o pneu reserva
print("\n### Trocar Pneu Verificando Reserva ###")
troca_pneus.trocar_pneu_verificando_reserva()

# Simular a verificação e troca de pneu furado
print("\n### Verificar e Trocar Pneu Furado ###")
troca_pneus.verificar_e_trocar_pneu_furado()