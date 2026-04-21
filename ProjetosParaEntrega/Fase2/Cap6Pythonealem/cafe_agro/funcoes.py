import json
from datetime import datetime

margem = ' ' * 4


def exibir_cabecalho(titulo):
    linha = '=' * 50
    print(linha)
    print(f'  {titulo}')
    print(linha)


def calcular_perda(sacas_esperadas, sacas_obtidas):
    if sacas_esperadas <= 0:
        return 0.0

    perda = ((sacas_esperadas - sacas_obtidas) / sacas_esperadas) * 100
    return round(max(perda, 0.0), 2)


def classificar_qualidade(perda_pct):
    if perda_pct <= 3.0:
        return 'Especial'
    elif perda_pct <= 7.0:
        return 'Superior'
    elif perda_pct <= 12.0:
        return 'Fino'
    else:
        return 'Comercial'


def calcular_rendimento(sacas, hectares):
    if hectares <= 0:
        raise ValueError('Hectares deve ser maior que zero.')
    return round(sacas / hectares, 2)


def validar_positivo(valor, campo):
    if valor <= 0:
        raise ValueError(f'O campo "{campo}" deve ser maior que zero.')


def salvar_relatorio_txt(lista_lotes):
    nome_arquivo = 'relatorio_colheita_cafe.txt'

    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arq:
            arq.write('=' * 55 + '\n')
            arq.write('  RELATÓRIO DE COLHEITA DE CAFÉ\n')
            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")
            arq.write(f'  Gerado em: {data_hora}\n')
            arq.write('=' * 55 + '\n\n')

            if not lista_lotes:
                arq.write('  Nenhum lote cadastrado.\n')
            else:
                for lote in lista_lotes:
                    arq.write(f'  ID        : {lote[0]}\n')
                    arq.write(f'  Fazenda   : {lote[1]}\n')
                    arq.write(f'  Variedade : {lote[2]}\n')
                    arq.write(f'  Sacas     : {lote[3]}\n')
                    arq.write(f'  Qualidade : {lote[4]}\n')
                    arq.write(f'  Perda %   : {lote[5]}%\n')
                    arq.write(f'  Rendimento: {lote[6]} sc/ha\n')
                    arq.write(f'  Data      : {lote[7]}\n')
                    arq.write('-' * 55 + '\n')

                arq.write(f'\nTotal de lotes: {len(lista_lotes)}\n')

        print(f'\n{margem}Relatório gerado com sucesso.')

    except IOError as erro:
        print(f'\n{margem}Erro ao gerar relatório: {erro}')


def salvar_backup_json(lista_lotes):
    nome_arquivo = 'backup_lotes_cafe.json'

    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arq:
            json.dump(lista_lotes, arq, ensure_ascii=False, indent=4)

        print(f'\n{margem}Backup salvo com sucesso.')

    except IOError as erro:
        print(f'\n{margem}Erro ao salvar JSON: {erro}')


def carregar_backup_json():
    nome_arquivo = 'backup_lotes_cafe.json'

    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arq:
            return json.load(arq)

    except (FileNotFoundError, json.JSONDecodeError):
        return []