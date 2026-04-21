# Sistema de Gestão de Colheita de Café

## Sobre o projeto

Este projeto foi desenvolvido para a disciplina de Python e Agronegócio da FIAP.

A ideia foi criar um sistema simples para registrar lotes de colheita de café e calcular automaticamente algumas informações importantes, como perda na colheita, qualidade do lote e rendimento por hectare.

Também foi implementada a geração de relatório em arquivo TXT e backup em JSON.

## Contexto

O café é um dos produtos mais importantes do agronegócio brasileiro, e pequenas perdas durante a colheita já impactam diretamente o resultado do produtor.

Pensando nisso, o sistema foi desenvolvido para organizar esses dados e facilitar o acompanhamento da produção.

## Funcionalidades

* Cadastro de lote de colheita
* Cálculo automático de perda (%)
* Classificação da qualidade do lote
* Cálculo de rendimento por hectare
* Listagem dos lotes cadastrados
* Geração de relatório em TXT
* Backup dos dados em JSON

## Estrutura do projeto

cafe_agro/
├── gs_cafe.py
├── funcoes.py
├── Script_Oracle.sql
└── README.md

## Como executar

1. Abrir o terminal na pasta do projeto
2. Executar o comando:

python3 gs_cafe.py

## Sobre o banco de dados

O projeto também possui integração com banco de dados Oracle, incluindo o script de criação da tabela no arquivo Script_Oracle.sql.

No entanto, devido à indisponibilidade do ambiente no momento, a execução foi realizada utilizando armazenamento local com JSON.

## Observação

As credenciais de banco não foram utilizadas na execução atual por conta de problemas de conexão no ambiente Oracle.

## Autor

Lucas Henrique Aparecido Gomes de Mello
RM569583
FIAP — 1TIAOB — Fase 2
