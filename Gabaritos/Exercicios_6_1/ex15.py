# Solicita o nome do aluno
nome_aluno = input("Digite o nome do aluno: ")

# Solicita as notas das três matérias
nota_matematica = float(input("Digite a nota de Matemática: "))
nota_portugues = float(input("Digite a nota de Português: "))
nota_historia = float(input("Digite a nota de História: "))

# Verifica se todas as notas são maiores que 7
aprovado = nota_matematica >= 7 and nota_portugues >= 7 and nota_historia >= 7

# Exibe o resultado
if aprovado:
    print(f"Parabéns, {nome_aluno}! Você foi aprovado(a)!!")
else:
    print(f"{nome_aluno}, infelizmente você não foi aprovado(a). Estude mais nas próximas avaliações.")