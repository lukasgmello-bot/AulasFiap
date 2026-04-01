# ------ DEFINIÇÃO DOS SUBALGORITMOS
def situacaoAluno(m) -> str:
    if m < 6:
        return "Reprovado"
    else:
        return "Aprovado"

# ------- PROGRAMA PRINCIPAL
media = float(input("Digite a média anual:"))
print(f"Você está {situacaoAluno(media)} com média {media}.")