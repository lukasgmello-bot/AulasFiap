"""
Sintaxe - Função
def <nomme função ([parâmetros]):
    <corpo da função>
    return valor

Exemplo: Retornar a quantidade de dolares a parti de um valor dado em reais
e a cotação do dolar
"""
#Criando Função
def totalEmDolar(qR: float, cD: float) -> None:
    resp = qR / cD
    return resp #200

#Programa Principal
qtdReais = float(input("Digite a quantidade de reais: "))# 1000
cotacaoDolar = float(input("Digite a cotação do dólar: ")) #5   
qtdDolares = totalEmDolar(qtdReais, cotacaoDolar)
print(f"A quantidade em Reais {qtdReais:.2f} = Quantia em dólares $  {totalEmDolar(qtdReais, cotacaoDolar):.2f}")