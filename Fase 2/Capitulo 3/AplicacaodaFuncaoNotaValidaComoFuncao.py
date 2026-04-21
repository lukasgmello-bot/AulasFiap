# ------ UTILIZANDO FUNÇÃO
def notaValida(nota: float) -> bool:
    # será analisada a expressão e resultará True ou False
    return nota >= 0 and nota <= 10

# ------- PROGRAMA PRINCIPAL
num = float(input("Nota: "))
while not notaValida(num):
    print(f"{num} é uma nota Inválida!")
    num = float(input("\nDigite uma nota entre 0 e 10: "))
print(f"Agora você digitou uma nota válida: {num}")