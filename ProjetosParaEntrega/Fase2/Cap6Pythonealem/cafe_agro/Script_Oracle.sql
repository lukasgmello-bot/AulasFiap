
-- SCRIPT ORACLE - SISTEMA DE GESTÃO DE COLHEITA DE CAFÉ
-- Execute este script no Oracle SQL Developer antes de rodar
-- o programa Python gs_cafe.py

-- Remove a tabela caso já exista (evita conflito)
BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE lotes_cafe';
EXCEPTION
    WHEN OTHERS THEN NULL;
END;
/

-- Criação da tabela de lotes de colheita de café
CREATE TABLE lotes_cafe (
    id               NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    fazenda          VARCHAR2(50)  NOT NULL,
    variedade        VARCHAR2(30)  NOT NULL,
    sacas            FLOAT         NOT NULL,
    qualidade        VARCHAR2(20)  NOT NULL,
    perda_percentual FLOAT         NOT NULL,
    rendimento_ha    FLOAT         NOT NULL,
    data_colheita    VARCHAR2(10)  NOT NULL
);

-- Verificação: exibe a estrutura da tabela criada
SELECT column_name, data_type, data_length
FROM user_tab_columns
WHERE table_name = 'LOTES_CAFE';
