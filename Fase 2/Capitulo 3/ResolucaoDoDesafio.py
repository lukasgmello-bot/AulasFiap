# ----------------- DEFINIÇÃO DOS SUBALGORITMOS
"""
Verifica se uma nota é válida ou não
PROTÓTIPO: notaValida(nota: Float): Boolean
"""
def notaValida(nota: float) -> bool:
    return nota >= 0 and nota <= 10


"""
Exibe uma mensagem de nota inválida
PROTÓTIPO: msgNotaInvalida(nota: Float): void
"""
def msgNotaInvalida(nota: float) -> None:
    print(f"A nota {nota} não é válida. \nDigite uma nota entre 0 e 10: ", end='')


"""
Retorna o menor entre três valores
PROTÓTIPO: menor3n(n1, n2, n3: Float): float
"""
def menor3n(n1, n2, n3: float) -> float:
    menor = n1
    if n2 < menor:
        menor = chk2
    if n3 < menor:
        menor = chk3
    return menor


"""
Calcular a média dos CheckPoints
PROTÓTIPO: mediaCheckpoints(n1, n2, n3: Real): Real
"""
def mediaCheckpoints(n1, n2, n3: float) -> float:
    return (n1 + n2 + n3 - menor3n(n1, n2, n3)) / 2


"""
Calcular a média de 2 valores
PROTÓTIPO: media2n(n1, n2: Real): Real
"""
def media2n(n1, n2: float) -> float:
    return (n1 + n2) / 2


"""
Calcular a porcentagem de um valor
PROTÓTIPO: porcentagemValor(valor, percentual: Real): Real
"""
def porcentagemValor(valor, percentual: float) -> float:
    return valor * percentual


"""
Calcular a soma de 3 numeros
PROTÓTIPO: soma3n(n1, n2, n3: Real): Real
"""
def soma3n(n1, n2, n3: float) -> float:
    return n1 + n2 + n3


"""
Calcular a soma de 2 numeros
PROTÓTIPO: soma2n(n1, n2: Real): Real
"""
def soma2n(n1, n2: float) -> float:
    return n1 + n2


"""
Exibe se está aprovado ou reprovado
PROTÓTIPO: exibeStatus(media: Real): String
"""
def exibeStatusFunc(media: float) -> str:
    if media >= 6:
        return "Aprovado!"
    elif media < 4:
        return "Reprovado!"
    else:
        return "Exame"


"""
Exibe se está aprovado ou reprovado
PROTÓTIPO: exibeStatus(media: Real): void
"""
def exibeStatusProc(media: float) -> None:
    if media >= 6:
        print("Aprovado!\n")
    elif media < 4:
        print("Reprovado!\n")
    else:
        print("Exame\n")


"""
Exibe a mensagem de Aprovado ou Reprovado depois do exame
PROTÓTIPO: msgAprovReprovExame(mf: Real): void
"""
def msgAprovReprovExame(mf: float) -> None:
    if mf < 6:
        print(f"Reprovado em exame com média {mfinal}")
    else:
        print(f"Aprovado em exame com média {mfinal}")


"""
Verifica se foi digitado S de Sim
PROTÓTIPO: continua(op: string): Lógico
"""
def continua(op: str) -> bool:
    return op == "S" or op == "s"


"""
Verifica se foi digitado S ou N de Sim ou Não
PROTÓTIPO: opcaoInvalida(op: string): Lógico
"""
def opcaoInvalida(op):
    return op != "s" and op != "S" and op != "n" and op != "N"


# ------------------------- PROGRAMA PRINCIPAL
opcao = 's'

while continua(opcao):

    print("---------------------- P R I M E I R O   S E M E S T R E")
    # Leitura dos checkPoints
    chk1 = float(input("Digite o checkpoint 1:"))
    while not notaValida(chk1):
        msgNotaInvalida(chk1)
        chk1 = float(input())

    chk2 = float(input("Digite o checkpoint 2:"))
    while not notaValida(chk2):
        msgNotaInvalida(chk2)
        chk2 = float(input())

    chk3 = float(input("Digite o checkpoint 3:"))
    while not notaValida(chk3):
        msgNotaInvalida(chk3)
        chk3 = float(input())

    # Calcula a média dos checkpoints do primeiro semestre
    mediaChk = mediaCheckpoints(chk1, chk2, chk3)
    print(f"Média dos checkpoints: {mediaChk:.1f}\n")

    # Leitura dos Sprints
    sprint1 = float(input("Digite o sprint 1:"))
    while not notaValida(sprint1):
        msgNotaInvalida(sprint1)
        sprint1 = float(input())

    sprint2 = float(input("Digite o sprint 2:"))
    while not notaValida(sprint2):
        msgNotaInvalida(sprint2)
        sprint2 = float(input())

    # Calculando a média dos Sprints
    mediaSprint = media2n(sprint1, sprint2)
    print(f"Média dos sprints: {mediaSprint:.1f}\n")

    # Lendo a  nota da prova semestral
    provaSemestral = float(input("Digite prova semestral:"))
    while not notaValida(provaSemestral):
        msgNotaInvalida(provaSemestral)
        provaSemestral = float(input())

    # Ponderando os valores das médias
    pontosChk = porcentagemValor(mediaChk, 0.2)
    pontosSprints = porcentagemValor(mediaSprint, 0.2)
    pontosSemestral = porcentagemValor(provaSemestral, 0.6)

    # Cálculo da média do primeiro semestre
    mediaPrimeiroSemestre = soma3n(pontosChk, pontosSprints, pontosSemestral)
    print(f"Média do primeiro semestre: {mediaPrimeiroSemestre:.2f}\n")

    # Pontos obtidos no primeiro semestre
    pontosPrimeiroSemestre = porcentagemValor(mediaPrimeiroSemestre, 0.4)

    print("---------------------- S E G U N D O   S E M E S T R E")
    # Leitura dos checkPoints
    chk1 = float(input("Digite o checkpoint 1:"))
    while not notaValida(chk1):
        msgNotaInvalida(chk1)
        chk1 = float(input())

    chk2 = float(input("Digite o checkpoint 2:"))
    while not notaValida(chk2):
        msgNotaInvalida(chk2)
        chk2 = float(input())

    chk3 = float(input("Digite o checkpoint 3:"))
    while not notaValida(chk3):
        msgNotaInvalida(chk3)
        chk3 = float(input())

    # Calcula a média dos checkpoints do primeiro semestre
    mediaChk = mediaCheckpoints(chk1, chk2, chk3)
    print(f"Média dos checkpoints: {mediaChk:.1f}\n")

    # Leitura dos Sprints
    sprint1 = float(input("Digite o sprint 1:"))
    while not notaValida(sprint1):
        msgNotaInvalida(sprint1)
        sprint1 = float(input())

    sprint2 = float(input("Digite o sprint 2:"))
    while not notaValida(sprint2):
        msgNotaInvalida(sprint2)
        sprint2 = float(input())

    # Calculando a média dos Sprints
    mediaSprint = media2n(sprint1, sprint2)
    print(f"Média dos sprints: {mediaSprint:.1f}\n")

    # Lendo a  nota da prova semestral
    provaSemestral = float(input("Digite prova semestral:"))
    while not notaValida(provaSemestral):
        msgNotaInvalida(provaSemestral)
        provaSemestral = float(input())

    # Ponderando os valores das médias
    pontosChk = porcentagemValor(mediaChk, 0.2)
    pontosSprints = porcentagemValor(mediaSprint, 0.2)
    pontosSemestral = porcentagemValor(provaSemestral, 0.6)

    # Cálculo da média do primeiro semestre
    mediaSegundoSemestre = soma3n(pontosChk, pontosSprints, pontosSemestral)
    print(f"Média do segundo semestre: {mediaSegundoSemestre:.2f}\n\n")

    # Pontos obtidos no primeiro semestre
    pontosSegundoSemestre = porcentagemValor(mediaSegundoSemestre, 0.6)

    # Cálculo da média final
    mediaFinal = soma2n(pontosPrimeiroSemestre, pontosSegundoSemestre)

    print(f"Média final: {mediaFinal:.1f} - ", end="")

    exibeStatusProc(mediaFinal)
    if exibeStatusFunc(mediaFinal) == "Exame":
        # Leitura dos Sprints
        notaExame = float(input("Digite a nota do exame:"))
        while not notaValida(notaExame):
            msgNotaInvalida(notaExame)
            notaExame = float(input())
        mfinal = media2n(mediaFinal, notaExame)
        msgAprovReprovExame(mfinal)

    opcao = input("Calcular a média de outro aluno? [S]im ou [N]ão.")
    while opcaoInvalida(opcao):
        opcao = input("ERRO! Digite [S]im ou [N]ão:")

    print('''
        Obrigado por utilizar o nosso programa!
    ''')