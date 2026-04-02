"""
Sintaxe - com parâmetro default:
def <nome do subalgoritmo (parâmetro = valor_padrão):
<corpo do subalgoritmo>
return valor
"""
#Exemplo: Criando a função com parametros default
def potencia(base = 2, expoente = 2):
	return base  ** expoente

#Programa Principal
print (f"Potencia = {potencia(3, 4)}")
print (f"Potencia = {potencia()}")
print (f"Potencia = {potencia(expoente= 5)}")
print (f"Potencia = {potencia(4,5)}")