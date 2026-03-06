"""
if <condição>:
    <bloco verdadeiro

Exemplo:
Fazer um algoritmo que leia a compra de um usuário.
Caso ela seja acima de 300 reais efetuar o desconto de 10% e
exibir o valor da compra atualizada

Entrada: 400  Saída: 360
Entrada: 150  Saída: 150
"""

#ler a compra do usuário
compra = float(input('Valor da compra: '))

#se a compra for maior do que 300
if compra > 300:

    #efetua o desconto de 10%
    compra = compra * 0.9
# exibir o valor atualizado
print(f"Compra {compra:.2f}")