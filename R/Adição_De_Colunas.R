#Carregue a biblioteca dplyr
install.packages(dplyr)
library(dplyr)

#Crie um data frame com valores ausentes
vendas_loja <- data.frame(
  data_venda = c("2026-01-01", "2026-01-02", "2026-01-03", "2026-01-04", "2026-01-05"),
  produto = c("A", "B", "A", NA, "c"),
  quantidade = c(10, 15, 20, 20, 25),
  receita = c(100, 150, 200, 200, 250)
)

#Mostrar resultado
print(vendas_loja)

#Identifique e conte os valores ausentes em cada coluna
valores_ausentes <- colSums(is.na(vendas_loja))

#Mostrar resultado
print(valores_ausentes)

#1. Calcule a média da quantidade vendida
media_quantidade <- vendas_loja %>%