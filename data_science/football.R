# install.packages("XML")
# install.packages("RSQLite")
# install.packages("stringr")
# install.packages("ggplot2")
library(XML)
library(RSQLite)
library(stringr)
library(ggplot2)

getOffense <- function(){
    year <- 2013
    
    url <-
        paste("http://sports.yahoo.com/nfl/stats/byteam?group=Offense&
cat=Total&conference=NFL&year=season_",year,"&sort=530&old_cat
egory=Total&old_group=Offense")
    
    offense <- readHTMLTable(url, encoding = "UTF-8",
                             colClasses="character")[[7]]
    return(offense)
}

offense <- getOffense()


