"""
Exemplo 01. Sim ou Não
utilizando o laço Enquanto (while)

resp = input("Digite [S]im ou [N]ão: ")
while resp != 'S' and resp != 'N':
    print("Opção inválida! Digite [S]im ou [N]ão.")
    resp = input()
print("Você digitou a letra válida", resp)
"""

# Mesmo exemplo utilizando o laço while com operador de associação
resp = input("Digite [S]im ou [N]ão: ")
while resp not in ['S', 'N']:
    print("Opção inválida! Digite [S]im ou [N]ão.")
    resp = input()
print("Você digitou a letra válida", resp)