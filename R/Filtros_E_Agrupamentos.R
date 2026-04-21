#Instalar e carregar o pacote dplyr
install.packages("dplyr")
library("dplyr")

#Criar dados
data_frame <- data.frame(
  idade = c(30, 25, 35, 50, 15, 20),
  genero = c(0, 0, 1, 1, 0, 1)
)

#Mostrar resultado
print(data_frame)

#Filtrar dados: selecionar apenas linhas onde a idade seja maior que 25
# a intrução para fazer filtro sempre será %>%
dados_filtrados <- data_frame %>% filter (idade > 25)

#Mostrar resultado
print(dados_filtrados)

#Agrupar dados por genêro e calcular média de idade por grupo
dados_agrupados <- data_frame %>% group_by(genero) %>%summarize(media_idadei = mean(idade))

#Visualizar resultado
print(dados_agrupados)