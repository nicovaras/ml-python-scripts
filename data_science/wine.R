wine <- read.csv("goodwine.csv")
summary(wine)

#install.packages("doSNOW")
library(doSNOW)
registerDoSNOW(makeCluster(8, type = "SOCK"))

#install.packages("corrplot")
library(corrplot)
corrplot(cor(wine[, -c(13, 15)]), method = "number", tl.cex = 1.0)

library(caret)
set.seed(1234) #so that the indices will be the same when re-run
trainIndices = createDataPartition(wine$good, p = 0.8, list = F)
wanted = !colnames(wine) %in% c("free.sulfur.dioxide", "density", "quality",
                                "color", "white")
wine_train = wine[trainIndices, wanted] #remove quality and color, as well as density and others
wine_test = wine[-trainIndices, wanted]

wine_trainplot = predict(preProcess(wine_train[,-10], method="range"),
                         wine_train[,-10])
featurePlot(wine_trainplot, wine_train$good, "box")