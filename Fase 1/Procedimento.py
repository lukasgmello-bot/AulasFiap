"""
Sintaxe - Procedimento:
def <nome procedimento>([parâmetros]):
    <corpo do procedimento>

Exemplo: Exibir os números em ordem crescente:
"""
#Criação do procedimento
def exibir_ordenados(num1, num2):
    if num1 < num2:
        print(f"{num1} e {num2}")
    else:   
        print(f"{num2} e {num1}")

#Programa principal

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
exibir_ordenados(n1, n2)