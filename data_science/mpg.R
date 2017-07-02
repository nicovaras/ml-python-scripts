# Notas:
# * read.csv para leer csv, siempre con stringsAsFactors = F para que no los tome como categoricos

# Chapter 2 MPG
download.file(
  "http://www.fueleconomy.gov/feg/epadata/vehicles.csv.zip",
  "/tmp/vehicles.csv.zip"
)

library(plyr)
library(ggplot2)
library(reshape2)

vehicles <- read.csv(unzip("/tmp/vehicles.csv.zip", "vehicles.csv"),
                     stringsAsFactors = F)
labels <- read.table("varlabels.txt", sep = "-", header =
                       FALSE)

mpgByYr <- ddply(vehicles, ~year, summarise, avgMPG =
                   mean(comb08), avgHghy = mean(highway08), avgCity =
                   mean(city08))

ggplot(mpgByYr, aes(year, avgMPG)) + geom_point() +
  geom_smooth() + xlab("Year") + ylab("Average MPG") +
  ggtitle("All cars")

ggplot(byYear2, aes(year, value)) + geom_point() +
    geom_smooth() + facet_wrap(~variable, ncol = 1, scales =
                                   "free_y") + xlab("Year") + ylab("")


gasCars4 <- subset(gasCars, cylinders == "4")
ggplot(gasCars4, aes(factor(year), comb08)) + geom_boxplot() + 
    facet_wrap(~trany2, ncol = 1) + 
    theme(axis.text.x = element_text(angle = 45)) + 
    labs(x = "Year", y = "MPG")


ggplot(gasCars4, aes(factor(year), fill = factor(trany2))) +
    geom_bar(position = "fill")

library(plyr)

carsMake <- ddply(gasCars4, ~year, summarise, numberOfMakes =
                      length(unique(make)))
ggplot(carsMake, aes(year, numberOfMakes)) + geom_point() +
    labs(x = "Year", y = "Number of available makes") + ggtitle("Four
cylinder cars")