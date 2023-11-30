def verifica_parenteses(expressao):
    pilha = []
    
    for caractere in expressao:
        if caractere == '(':
            pilha.append(caractere)
        elif caractere == ')':
            if not pilha or pilha[-1] != '(':
                return False
            pilha.pop()
    
    return len(pilha) == 0

# Teste a função
expressao1 = "(2 + 3) * (4 - 1)"
expressao2 = "((5 + 6) * (7 - 2)"
expressao3 = "())("

print(verifica_parenteses(expressao1))  # True
print(verifica_parenteses(expressao2))  # False
print(verifica_parenteses(expressao3))  # False
