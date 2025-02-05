# Se importan las librerías necesarias
library(dplyr)
library(ggplot2)

# Se lee el dataset
athletes_data <- read.csv("C:/Users/Miguel Gómez/Desktop/Universidad/MASTER/Ciclo de vida de los datos/practica workflow/Forbes.csv")

# Se renombra la columna con simbología problemática
colnames(athletes_data)[8] <- "earnings_million_dollars"

# Se agrupan los atletas por año y se calcula la media de ganancias para cada grupo
athletes_by_year <- group_by(athletes_data, Year)
mean_earnings_by_year <- summarise(athletes_by_year, mean_earnings = mean(earnings_million_dollars))

# Se crea un gráfico para visualizar la evolución temporal de las ganancias
ggplot(mean_earnings_by_year, aes(Year, mean_earnings)) +
  geom_line() +
  xlab("Year") +
  ylab("Mean earnings ($ million)") +
  ggtitle("Temporal Analysis of the Earnings of the Top 10 Athletes per Year")
