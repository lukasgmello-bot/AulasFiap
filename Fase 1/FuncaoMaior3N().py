# --- DEFINIÇÃO DO SUBALGORITMO
def maior3n(n1, n2, n3):
    maior = n1
    if n2 > maior:
        maior = n2
    if n3 > maior:
        maior = n3
    return maior

# --- PROGRAMA PRINCIPAL
print("Exibindo o maior entre 3 números com função própria")
print(f"Maior valor entre 45, 83 e 33: {maior3n(45,83,33)}")