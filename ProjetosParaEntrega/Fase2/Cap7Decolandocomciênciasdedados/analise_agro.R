# Lucas Henrique Aparecido Gomes de Mello - RM569583 - Fase 2 - Capítulo 9

setwd("/Users/LeticiaFerre/AulasFiap/ProjetosParaEntrega/Fase2/Cap7Decolandocomciênciasdedados")

# Ler a base de dados
dados <- read.csv("dados_agro.csv", header = TRUE, sep = ",")

# Mostrar as primeiras linhas
print("Primeiras linhas da base:")
print(head(dados))

# Estrutura dos dados
print("Estrutura da base:")
print(str(dados))


# ANALISE DA VARIAVEL QUANTITATIVA
# Variavel escolhida: Producao_kg_ha


producao <- dados$Producao_kg_ha

# Medidas de tendencia central
media <- mean(producao)
mediana <- median(producao)

print("Medidas de Tendencia Central:")
print(paste("Media:", media))
print(paste("Mediana:", mediana))

# Moda
tabela_freq <- table(producao)
moda <- as.numeric(names(tabela_freq)[tabela_freq == max(tabela_freq)])

print("Moda(s):")
print(moda)

# Medidas de dispersao
variancia <- var(producao)
desvio_padrao <- sd(producao)
amplitude <- max(producao) - min(producao)

print("Medidas de Dispersao:")
print(paste("Variancia:", variancia))
print(paste("Desvio padrao:", desvio_padrao))
print(paste("Amplitude:", amplitude))

# Medidas separatrizes
quartis <- quantile(producao)
quintis <- quantile(producao, probs = seq(0, 1, 0.2))
decis <- quantile(producao, probs = seq(0, 1, 0.1))

print("Quartis:")
print(quartis)

print("Quintis:")
print(quintis)

print("Decis:")
print(decis)


# ANALISE GRAFICA DA VARIAVEL QUANTITATIVA


hist(producao,
     main = "Histograma da Producao por hectare",
     xlab = "Producao (kg/ha)",
     ylab = "Frequencia",
     col = "lightblue",
     border = "black")

boxplot(producao,
        main = "Boxplot da Producao por hectare",
        ylab = "Producao (kg/ha)",
        col = "lightgreen")


# ANALISE DA VARIAVEL QUALITATIVA
# Variavel escolhida: Cultura


tabela_cultura <- table(dados$Cultura)

print("Frequencia da variavel Cultura:")
print(tabela_cultura)

barplot(tabela_cultura,
        main = "Distribuicao das Culturas",
        xlab = "Cultura",
        ylab = "Frequencia",
        col = "orange")