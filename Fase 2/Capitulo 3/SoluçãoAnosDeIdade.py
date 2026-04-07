# ------ DEFINIÇÃO DOS SUBALGORITMOS
def anosDeIdade(anoNascimento) -> int:
    idade = 2026 - anoNascimento
    return idade

# ------- PROGRAMA PRINCIPAL
ano = int(input("Digite o ano do seu nascimento:"))
print(f"Você tem {anosDeIdade(ano)} anos.")