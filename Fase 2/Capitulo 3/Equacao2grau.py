"""
Utilizando arquivos externos

"""

import math

#Criando Subalgoritmos
def calcularDelta(a, b, c):
    return b**2 - 4*a*c

def calcularX1(a, b, c):
    returno (-b + math.sqrt(calcularDelta(a, b, c))) / (2*a)

def calcularX2(a, b, c):
    return (-b - math.sqrt(calcularDelta(a, b, c))) / (2*a)

def exibeRaizes (a, b, c):
    print(f"x1 = {calcularX1(a, b, c)}")
    print(f"x2 = {calcularX2(a, b, c)}")