km = int(input("Digite a quantidade de quilometros percorridos: "))
dias = int(input("Digite quantos dias você ficou com o carro: "))

preço_por_dia = 89
preço_por_km = 0.15
preço_a_pagar = km * preço_por_km + dias * preço_por_dia

print("Total a pagar: R$ %7.2f" % preço_a_pagar)