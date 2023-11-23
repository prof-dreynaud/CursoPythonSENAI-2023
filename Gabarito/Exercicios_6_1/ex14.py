cigarros_por_dia = int(input("Quantidade de cigarros por dia: "))
anos_fumando = float(input("Quantidade de anos fumando: "))

redução_em_minutos = anos_fumando * 365 * cigarros_por_dia * 10

# Um dia tem 24 x 60 minutos
redução_em_dias = redução_em_minutos / (24 * 60)

print("Redução do tempo de vida %8.2f dias." % redução_em_dias)