contagemAprovados = 0
qtdAlunos = 40
aluno = 1
while aluno <= qtdAlunos:
    # P R I M E I R O   S E M E S T R E
    print(f"------------------------------- ALUNO: {aluno}")
    print("PRIMEIRO SEMESTRE")
    # Leitura dos checkpoints
    chk1 = float(input("Digite o Checkpoint 1:"))
    chk2 = float(input("Digite o Checkpoint 2:"))
    chk3 = float(input("Digite o Checkpoint 3:"))
    # Verificando o Checkpoint de menor valor
    menor = chk1
    if chk2 < menor:
        menor = chk2
    if chk3 < menor:
        menor = chk3
    # Calculando a média dos Checkpoints
    mediaChk = (chk1 + chk2 + chk3 - menor) / 2
    # Leitura dos Sprints
    sprint1 = float(input("Digite o Sprint 1:"))
    sprint2 = float(input("Digite o Sprint 2:"))
    # Calculando a média dos Sprints
    mediaSprint = (sprint1 + sprint2) / 2
    # Leitura da prova semestral
    semestral = float(input("Digite prova semestral:"))
    # Ponderando os valores das médias
    pontosChk = mediaChk * 0.2
    pontosSprints = mediaSprint * 0.2
    pontosSemestral = semestral * 0.6
    # Cálculo da média do primeiro semestre
    mediaPrimeiroSemestre = (pontosChk + pontosSprints + pontosSemestral)
    # Pontos obtidos no primeiro semestre
    pontosPrimeiroSemestre = mediaPrimeiroSemestre * 0.4

    # S E G U N D O   S E M E S T R E
    print("SEGUNDO SEMESTRE")
    # Leitura dos checkpoints
    chk1 = float(input("Digite o Checkpoint 1:"))
    chk2 = float(input("Digite o Checkpoint 2:"))
    chk3 = float(input("Digite o Checkpoint 3:"))
    # Verificando o Checkpoint de menor valor
    menor = chk1
    if chk2 < menor:
        menor = chk2
    if chk3 < menor:
        menor = chk3
    # Calculando a média dos Checkpoints
    mediaChk = (chk1 + chk2 + chk3 - menor) / 2
    # Leitura dos Sprints
    sprint1 = float(input("Digite o Sprint 1:"))
    sprint2 = float(input("Digite o Sprint 2:"))
    # Calculando a média dos Sprints
    mediaSprint = (sprint1 + sprint2) / 2
    # Leitura da prova semestral
    semestral = float(input("Digite prova semestral:"))
    # Ponderando os valores das médias
    pontosChk = mediaChk * 0.2
    pontosSprints = mediaSprint * 0.2
    pontosSemestral = semestral * 0.6
    # Cálculo da média do segundo semestre
    mediaSegundoSemestre = (pontosChk + pontosSprints + pontosSemestral)
    # Pontos obtidos no segundo semestre
    pontosSegundoSemestre = mediaSegundoSemestre * 0.6

    # Exibição da média do primeiro semestre
    print (f"\nMédia do Primeiro Semestre: {mediaPrimeiroSemestre:.1f}")
    # Exibição da média do segundo semestre
    print (f"Média do Segundo Semestre: {mediaSegundoSemestre:.1f}")
    # Cálculo da média final
    mediaFinal = pontosPrimeiroSemestre + pontosSegundoSemestre
    print (f"Média Final: {mediaFinal:.1f} - ", end="")
    if mediaFinal >= 6:
        contagemAprovados += 1
        print("Aprovado!")
    else:
        print("Não Aprovado!")
    aluno += 1

# Exibição da Quantidade de Alunos Aprovados
print("Quantidade de aprovados: ", contagemAprovados)