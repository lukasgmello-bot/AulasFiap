"""
Programa Prinicipal

"""
#Forma 1: Necessita que todos os subalgoritmos sejam iniciados pelo nome do arquivo
#import Equacao2grau

# Froma 2: Importando o subalgoritmo desejado
#from Equacao2grau import calcularDelta
#import Equacao2grau

#Fomra 3: Importando todos os subalgoritmos de uma vez
from Equacao2grau import *
import Equacao2grau  

print(f"Calculando o Delta: {Equacao2grau.calcularDelta(1, 12, -3)}")