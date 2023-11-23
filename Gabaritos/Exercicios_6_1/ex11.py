distância = float(input("Digite a distância em km:"))
velocidade_média = float(input("Digite a velocidade média em km/h:"))
tempo = distância / velocidade_média

print("O tempo estimado é de %5.2f horas" % tempo)

# Opcional: imprimir o tempo em horas, minutos e segundos
tempo_s = int(tempo * 3600)  # convertemos de horas para segundos
horas = int(tempo_s / 3600)  # parte inteira
tempo_s = int(tempo_s % 3600)  # o resto
minutos = int(tempo_s / 60)
segundos = int(tempo_s % 60)

print("%05d:%02d:%02d" % (horas, minutos, segundos))