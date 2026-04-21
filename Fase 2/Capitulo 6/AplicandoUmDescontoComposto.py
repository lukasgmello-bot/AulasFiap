"""
<bloco falso>

Exemplo:
Fazer um algoritimo que leia a compra de um usuário.
Caso ela seja acima de 300 reais efetuar o desconto de 10%
senao, efetuar um desconto de 5%.
Exibir o valor da compra atualizado
Entrada: 100  Saída: 95
Entrada: 400  Saída: 360
"""
#ler a compra
compra = float(input("Digite o valor da compra: "))

#se comprou acima de 300
if compra > 300:

#   efetuar o desconto de 10%
    compra_com_desconto = compra * 0.9

#senão
else:

#efetuar o desconto de 5%
    compra_com_desconto = compra * 0.95

#ebibir o valor com desconto
print(f"Valor da compra...: R$ {compra:.2f}\nValor tualizado...: R$ {compra_com_desconto:.2f}")