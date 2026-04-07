"""
if <condição>:
    <bloco verdadeiro>
else:
    <bloco falso>

Exemplo:
Dado 2 números, exibir o de maior valor
Entrada: 23 56  Saída:56
Entrada: 33 10  Sáida:33
"""

#ler o primeiro numero
num1 = int(input("Digite o primeiro número: "))

#ler o segundo numero
num2 = int(input("Digite o segundo número: "))

#se o primeiro numero for maior que o segundo
if num1 > num2:

#   exibir o primeiro
    print(num1)

#se não
else:

#   exibir o segundo numero
    print(num2)