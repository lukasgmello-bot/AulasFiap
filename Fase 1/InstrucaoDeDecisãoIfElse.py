"""
Sintaxe: Se então senão no Python

if <condição>:
    <bloco verdadeiro>
else:
    <bloco falso>

Exemplo?
Dada a idade do usuário, informar se ele é "Maior de idade" ou "Menor de idade"

Entrada: 40   Saída: Maior de idade
Entrada: 17   Sáida: Menor de idade

"""

#ler a idade do usuário
idade = int(input("Digite sua idade: "))

#se for de maior
if idade >= 18:

    #exibir maior de idade
    print(f"Maior de idade: {idade}")

#senão
else:

#exibir menor de idade
    print(f"Menor de idade: {idade}")