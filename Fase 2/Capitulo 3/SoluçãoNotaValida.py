# ------ DEFINIÇÃO DOS SUBALGORITMOS
def notaValida(n) -> bool:
    if n >= 0 and n <= 10:
        return True
    else:
        return False

# ------- PROGRAMA PRINCIPAL
nota = float(input("Digite uma nota: "))
if notaValida(nota):
    print(f"A nota {nota} é válida.")
else:
    print(f"A nota {nota} é inválida.")