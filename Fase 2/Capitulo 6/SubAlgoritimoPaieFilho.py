"""
Exemplo: Dados os valores de a, b e c por parâmetro, calcular a equação do 2º grau, ou seja, calcular o valor de x, onde x = (-b ± √(b² - 4ac)) / 2a
(Pai) e delta (Filho).
Subalgoritmos pai, filho (neto, bisnete ... ) são dependencias de subalgoritmos

"""
#Criação dos subalgoritimos dependentes

#Ler os valores
import math

def preencheValores() -> None:
    global ValorA, ValorB, ValorC
    ValorA = float(input("A: "))
    ValorB = float(input("B: "))
    ValorC = float(input("C: "))

#Calcular o delta
def calcularDelta(a, b, c:float) -> float:
    return b ** 2 - 4 * a * c

#Calcular o valor de x1
def calcularX1(a, b, c:float) -> float:
    return (-b + math.sqrt(calcularDelta(a, b, c)) / (2 * a))
#Calcular o valor de x2
def calcularX2(a: float, b: float, c: float) -> float:
    return (-b - math.sqrt(calcularDelta(a, b, c)) / (2 * a))

#exibir as raizes
def exibirResultados(d: float, x1: float, x2: float) -> None:
    print("Delta: = ", d)
    print("X1: = ", x1)
    print("X2: = ", x2)

#Programa Principal
ValorA = ValorB = ValorC = 0
preencheValores()

exibirResultados(calcularDelta(ValorA, ValorB, ValorC),\
calcularX1(ValorA, ValorB, ValorC),
calcularX2(ValorA, ValorB, ValorC)
)
