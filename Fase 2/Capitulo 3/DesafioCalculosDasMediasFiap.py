def ler_nota(nome):
    while True:
        nota = float(input(f"Digite {nome}: "))
        if 0 <= nota <= 10:
            return nota
        print("Nota inválida! Digite entre 0 e 10.")


def calcular_mcp(n1, n2, n3):
    notas = [n1, n2, n3]
    notas.sort(reverse=True)
    return (notas[0] + notas[1]) / 2


def calcular_ms(s1, s2):
    return (s1 + s2) / 2


def calcular_media_semestral(mcp, ms, gs):
    return (mcp * 2 + ms * 2 + gs * 6) / 10


def calcular_media_anual(m1, m2):
    return (m1 * 4 + m2 * 6) / 10


def verificar_status(ma):
    if ma >= 6:
        print(f"Média: {ma:.2f} - Aprovado")
    elif ma < 4:
        print(f"Média: {ma:.2f} - Reprovado")
    else:
        print(f"Média: {ma:.2f} - Exame")
        ne = ler_nota("Nota de Exame")
        mf = (ma + ne) / 2
        print(f"Média Final: {mf:.2f}")
        if mf >= 6:
            print("Aprovado após exame")
        else:
            print("Reprovado após exame")


def main():
    # 1º semestre
    cp1 = ler_nota("CP1")
    cp2 = ler_nota("CP2")
    cp3 = ler_nota("CP3")
    mcp1 = calcular_mcp(cp1, cp2, cp3)

    s1 = ler_nota("S1")
    s2 = ler_nota("S2")
    ms1 = calcular_ms(s1, s2)

    gs1 = ler_nota("GS1")

    m1 = calcular_media_semestral(mcp1, ms1, gs1)

    # 2º semestre
    cp4 = ler_nota("CP4")
    cp5 = ler_nota("CP5")
    cp6 = ler_nota("CP6")
    mcp2 = calcular_mcp(cp4, cp5, cp6)

    s3 = ler_nota("S3")
    s4 = ler_nota("S4")
    ms2 = calcular_ms(s3, s4)

    gs2 = ler_nota("GS2")

    m2 = calcular_media_semestral(mcp2, ms2, gs2)

    # média anual
    ma = calcular_media_anual(m1, m2)

    # resultado final
    verificar_status(ma)


# execução com repetição
while True:
    main()
    op = input("Deseja continuar? [S/N]: ").upper()
    if op == "N":
        break