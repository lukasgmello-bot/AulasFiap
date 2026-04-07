"""
Sintaxe - com parametro indefinido *args:
def <nome do subalgoritmo > (*args):
    <corpo do subalgoritmo>
    [return valor]

Exemplo: Calcular a média de N valores
"""
#efinição da Função com parametros do tipo *ARGS
def mediaNs(*ars) -> float:
    soma = 0
    for n in ars:
        soma += n
    return soma / len(ars) #len() retorna o totla de elementos

# Programa Principal
print(f"Média: {mediaNs(5,6,4.9,8,9)}")