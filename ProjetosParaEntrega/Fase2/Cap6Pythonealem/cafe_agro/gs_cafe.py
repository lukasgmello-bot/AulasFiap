from funcoes import *
import pandas as pd

lotes = carregar_backup_json()


def cadastrar_lote():
    exibir_cabecalho("Cadastro de Lote")

    try:
        fazenda = input("Nome da fazenda: ")

        print("\n1 - Arábica\n2 - Robusta")
        op = int(input("Escolha a variedade: "))

        variedade = "Arábica" if op == 1 else "Robusta"

        sacas_esperadas = float(input("Sacas esperadas: "))
        sacas_obtidas = float(input("Sacas obtidas: "))
        hectares = float(input("Hectares: "))
        data = input("Data (dd/mm/aaaa): ")

        validar_positivo(sacas_esperadas, "sacas esperadas")
        validar_positivo(sacas_obtidas, "sacas obtidas")
        validar_positivo(hectares, "hectares")

        perda = calcular_perda(sacas_esperadas, sacas_obtidas)
        qualidade = classificar_qualidade(perda)
        rendimento = calcular_rendimento(sacas_obtidas, hectares)

        lote = [
            len(lotes) + 1,
            fazenda,
            variedade,
            sacas_obtidas,
            qualidade,
            perda,
            rendimento,
            data
        ]

        lotes.append(lote)
        print("\nLote cadastrado!")

    except ValueError as e:
        print(f"\nErro: {e}")


def listar_lotes():
    exibir_cabecalho("Lista de Lotes")

    if not lotes:
        print("Nenhum lote cadastrado.")
        return

    df = pd.DataFrame(lotes, columns=[
        "ID", "Fazenda", "Variedade", "Sacas",
        "Qualidade", "Perda (%)", "Rendimento", "Data"
    ])

    print(df)


def alterar_lote():
    exibir_cabecalho("Alterar Lote")

    try:
        id_lote = int(input("ID do lote: "))

        for lote in lotes:
            if lote[0] == id_lote:
                novas_sacas = float(input("Novas sacas: "))
                hectares = float(input("Hectares: "))

                perda = calcular_perda(novas_sacas, novas_sacas)
                qualidade = classificar_qualidade(perda)
                rendimento = calcular_rendimento(novas_sacas, hectares)

                lote[3] = novas_sacas
                lote[4] = qualidade
                lote[5] = perda
                lote[6] = rendimento

                print("Atualizado!")
                return

        print("Lote não encontrado.")

    except:
        print("Erro.")


def excluir_lote():
    id_lote = int(input("ID para excluir: "))

    for lote in lotes:
        if lote[0] == id_lote:
            lotes.remove(lote)
            print("Removido!")
            return

    print("Não encontrado.")


def menu():
    while True:
        print("\n1-Cadastrar 2-Listar 3-Alterar 4-Excluir 5-Relatório 6-Backup 7-Sair")
        op = input("Escolha: ")

        if op == '1':
            cadastrar_lote()
        elif op == '2':
            listar_lotes()
        elif op == '3':
            alterar_lote()
        elif op == '4':
            excluir_lote()
        elif op == '5':
            salvar_relatorio_txt(lotes)
        elif op == '6':
            salvar_backup_json(lotes)
        elif op == '7':
            break


menu()