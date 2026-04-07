"""
Sintaxe: Se Então (if) no Python

if<condição>:
    <bloco verdadeiro

Exemplo:
O módulo na matematica consiste em deixar um numero positivo.
Sendo assim:
    |45| = 45
    |-9| = 9
Dado um numero pelo o usuário, apresentar o seu módulo matematico.

Entrada: 13  Saída: 13
Entrada: -4  Saída: 4
"""
#usuário digita um numero
num=int(input("Digite um numero: "))

#se o numero for negativo
if num < 0:

#transformar em positivo
    num = num * -1

#apresentar o numero
print(f"Módulo = {num}")