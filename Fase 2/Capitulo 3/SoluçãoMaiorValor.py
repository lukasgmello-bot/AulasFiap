# ------- DEFINIÇÃO DOS SUBALGORITMOS
def maiorValor(n1, n2, n3):
    maior = n1
    if n2 > maior:
        maior = n2
    if n3 > maior:
        maior = n3
    return maior

# ------- PROGRAMA PRINCIPAL
print("Digite 3 números: ")
n1 = float(input(""))
n2 = float(input(""))
n3 = float(input(""))
print(f"Resp. c/ a função 'max()'.........: {max(n1, n2, n3)}")
print(f"Resp. c/ a função 'maiorValor()'..: {maiorValor(n1, n2, n3)}")