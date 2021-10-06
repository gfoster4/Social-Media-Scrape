#setwd("C:/Users/Greg Foster/Documents/LRA Files/Instagram Data")

# json support
library(rtweet)
library(rjson)
library(jsonlite)
library(ggplot2)
library(dplyr)
library(tidyr)
library(tidytext)
library(tm)
library(widyr)
library(igraph)
library(ggraph)
library(leaflet)
library(gganimate)
library(lubridate)
library(maps)
library(ggthemes)
library(sqldf)

options(stringsAsFactors = FALSE)

appname <- "Homeless Covid Analysis"
key <- "VUzlC9m0lMnwK6u2caOxHCz21"
secret <- "Bh1o2NwgV5ktjPAIrX7s0pZeQ81UJEdtNVslD8bCtXs1XiqOqT"
access_token <- "1313145117616877569-w6dAJsZuHmPFIgG3NsvT7uuxIsdAtZ"
access_secret <- "t5Dz9Hmx6uIFacsElVOeXA07XhUDhqtyxZIjZAqnENfh9"

twitter_token <- create_token(
  app = appname,
  consumer_key = key,
  consumer_secret = secret,
  access_token = access_token,
  access_secret = access_secret)


cht <- search_tweets(q = "#selfie OR #selfies", 
                      n = 18000, lang = "en",
                      include_rts = FALSE, type = "recent", parse = TRUE, retryonratelimit = TRUE)

chtdf <- data.frame(cht)

df <- chtdf[,-26:-90]

df$media_type <- as.vector(df$media_type)
str(df)

df1 <- df %>% filter(media_type == 'photo')
df1

date<-df1$created_at
dateList <- substring(date,9,10)
dateVec <- as.numeric(dateList)
dateVec

hist(dateVec, main="Selfies Posted Per Day", xlab="November", ylab="Selfies", include.lowest=TRUE, axes = TRUE)


library(ggplot2)
g <- ggplot(data=df1, aes(created_at)) +
  geom_histogram(color="black", fill="white") +
  labs(title="Selfies Posted Per Day (Nov 7th - Nov 16th") +
  theme(plot.title = element_text(hjust = 0.5)) +
  xlab("Date") +
  ylab("Selfies") +
  theme(panel.background = element_rect(fill = "darkgrey",
                                    colour = "darkgrey",
                                    size = 0.5, linetype = "solid"))
g

#The below values will change each time the program is run, comments were made when I originally 
#collected the data

length(dateVec)
photoVec <- rep(c("photo"), times = 2203) #needs to be changed to the length of dateVec
photoVec
length(photoVec)
dfVec<-data.frame(dateVec,photoVec)

seven<-sqldf("select dateVec from dfVec where dateVec ==7")
seven #6 total selfies posted on November 7th

eight<-sqldf("select dateVec from dfVec where dateVec ==8")
eight #270 total selfies posted on November 8th

nine<- sqldf("select dateVec from dfVec where dateVec == 9")
nine #292 total selfies posted on November 9th

ten<- sqldf("select dateVec from dfVec where dateVec == 10")
ten #285 total selfies posted on November 10th

eleven<- sqldf("select dateVec from dfVec where dateVec == 11")
eleven #293 total selfies posted on November 11th

twelve<- sqldf("select dateVec from dfVec where dateVec == 12")
twelve #294 total selfies posted on November 12th

thirteen<- sqldf("select dateVec from dfVec where dateVec == 13")
thirteen #329 total selfies posted on November 13th

fourteen<- sqldf("select dateVec from dfVec where dateVec == 14")
fourteen #300 total selfies posted on November 14th

fifteen<- sqldf("select dateVec from dfVec where dateVec == 15")
fifteen #288 total selfies posted on November 15th

sixteen<- sqldf("select dateVec from dfVec where dateVec == 16")
sixteen #298 total selfies posted on November 16th

