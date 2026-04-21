# DEFINIÇÃO DO SUBALGORITMO ITERATIVO
def contagemIterativa(inicio: float, limite: float) -> None:
    while inicio <= limite:
        print(inicio)
        inicio += 1
    else:
        print("Fim!")

# PROGRAMA PRINCIPAL
print("Executando a função iterativa...")
contagemIterativa(1, 5)