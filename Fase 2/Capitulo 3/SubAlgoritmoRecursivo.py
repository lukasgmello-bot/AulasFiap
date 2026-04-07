"""
Subalgoritmo Interativo e Recursivo
Fazer a contagem regressiva a partir de um valor

"""

#Criação dos Subalgoritmos recursivos
#Iterativa
def timerInterativo(t: int) -> None:
    for s in range(t, -1, -1):
        print(s)
        time.sleep(1)


#Recursiva
def timerRecursivo(t: int) -> None:
    if t != -1:
        print(t)
        time.sleep(1)
        timerRecursivo(t - 1)

#Programa Principal
import time
print("Forma Iterativa")
timerInterativo(3)
print("Forma Recursiva")
timerRecursivo(3)
