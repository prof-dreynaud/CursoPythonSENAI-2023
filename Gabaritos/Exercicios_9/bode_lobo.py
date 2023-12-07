class Estado:
    def __init__(self, homem, lobo, bode, alfafa):
        self.homem = homem
        self.lobo = lobo
        self.bode = bode
        self.alfafa = alfafa

    def __str__(self):
        return f"Homem: {self.homem}, Lobo: {self.lobo}, Bode: {self.bode}, Alfafa: {self.alfafa}"


def travessia_rio(estado_atual):
    print("Início:", estado_atual)

    # Levar o bode para o outro lado do rio
    estado_atual.bode = not estado_atual.bode
    estado_atual.homem = not estado_atual.homem
    print("Levar o bode para o outro lado do rio:", estado_atual)

    # Voltar sozinho para o lado inicial
    estado_atual.homem = not estado_atual.homem
    print("Voltar sozinho para o lado inicial:", estado_atual)

    # Levar o lobo para o outro lado do rio
    estado_atual.lobo = not estado_atual.lobo
    estado_atual.homem = not estado_atual.homem
    print("Levar o lobo para o outro lado do rio:", estado_atual)

    # Voltar com o bode
    estado_atual.bode = not estado_atual.bode
    estado_atual.homem = not estado_atual.homem
    print("Voltar com o bode:", estado_atual)

    # Levar a alfafa para o outro lado do rio
    estado_atual.alfafa = not estado_atual.alfafa
    estado_atual.homem = not estado_atual.homem
    print("Levar a alfafa para o outro lado do rio:", estado_atual)

    # Voltar sozinho para o lado inicial
    estado_atual.homem = not estado_atual.homem
    print("Voltar sozinho para o lado inicial:", estado_atual)

    # Levar o bode para o outro lado do rio
    estado_atual.bode = not estado_atual.bode
    estado_atual.homem = not estado_atual.homem
    print("Levar o bode para o outro lado do rio:", estado_atual)


# Estado inicial: homem, lobo, bode, alfafa todos do lado inicial
estado_inicial = Estado(True, True, True, True)

# Simulação da travessia
travessia_rio(estado_inicial)