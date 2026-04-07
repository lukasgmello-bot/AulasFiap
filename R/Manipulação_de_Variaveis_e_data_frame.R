nome <- 'Rafael'
nomeDois = 'Karina'

#criação do data frame
dataFrame <- data.frame(nome = c('Rafael', 'Karina'), idade = c(37, 35))
print(dataFrame)

#Renomear colunas
colnames(dataFrame)[colnames(dataFrame) == 'idade'] <- 'idadeProfessor'
print (dataFrame)
colnames(dataFrame)[colnames(dataFrame) == 'nome'] <- 'nomeProfessor'
print(dataFrame)

#Manipulação de variaveis

testeIdadeFrame <- dataFrame$idadeProfessor

#mostrar resultador
print(testeIdadeFrame)

#selecionar valores de uma coluna utilizando $
colunaSelecionadaNome <- dataFrame$nomeProfessor

#Mostrar resultado
print (colunaSelecionadaNome)

#Selecionar valores de uma coluna utilizando outra maneira
colunaSelecionada <- dataFrame[,c('nomeProfessor')]

#Motrar resultado
print (colunaSelecionada)

#Segundo Exemplo

colunaSelecionadaDois <- dataFrame$nomeProfessor

#Mostrar resultado
print (colunaSelecionadaDois)

#Mais um exemplo para selecionar coluna, nesse caso serão duas

#data frame exemplo
data_frame <- data.frame(
  nome = c("Alice", "Bob", "Charlie"),
  idade = c(30, 25, 35),
  cidade = c("Nova York", "Los Angeles", "Chicago")
)

#Mostrar resultado
print(data_frame)

#Seleciona várias colunas
duasColunasSelecionadas <- data_frame[, c("nome", "cidade")]

#Mostrar colunas selecionadas
print (duasColunasSelecionadas)

#Selecionar várias colunas
duasColunaSelecionada <- data_frame[, c("nome", "idade")]

#Mostrar resultado
print (duasColunaSelecionada)

#Para concluir. selecionando valores de uma coluna e mostrando em linha
testeSelecionar <- data_frame$nome

#Mostrar resultado
print (testeSelecionar)