# ------ UTILIZANDO PROCEDIMENTO
def notaValida(nota: float) -> None:
    if nota >= 0 and nota <= 10:
        print(f"A nota {nota} é válida.")
    else:
        print(f"A nota {nota} é inválida.")

# ------- PROGRAMA PRINCIPAL
# Chamando o procedimento
num = 7
notaValida(num)