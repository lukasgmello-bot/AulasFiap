# ------ UTILIZANDO FUNÇÃO
def notaValida(nota: float) -> bool:
    # esta expressão analisará a condição e resultará True ou False
    return nota >= 0 and nota <= 10

# ------- PROGRAMA PRINCIPAL
num = 7
resposta = notaValida(num)
if resposta == True: # Ou simplesmente 'if resposta:'
    print(f"A nota {num} é válida.")
else:
    print(f"A nota {num} é inválida.")