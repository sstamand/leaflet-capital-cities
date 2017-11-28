---
title: "Capital Cities"
author: "sstamand"
date: "November 26, 2017"
output: html_document
keep_md: yes
---

```{r setup, include=FALSE}
setwd("~/Coursera/Assignments/Course 9/course project 1")
knitr::opts_chunk$set(echo = TRUE)
library(leaflet)
```

## Description

This map shows the capital cities (marked by gold stars) for 200 nations in the world. The map was created by leaflets. The data was scraped using Python from Lucille M. Nixon Elementary website available at [this link][1]. The Python code is also stored in the GitHub repository.

[1]: http://www.lab.lmnixon.org/4th/worldcapitals.html "link to the dataset" 

```{r map}
city_data <- read.csv("city_data.csv", header = TRUE, colClasses = c("character", "numeric", "numeric"))
star_icon <- makeIcon(
  iconUrl = "star_icon.png",
  iconWidth = 25*215/230, iconHeight = 25,
  iconAnchorX = 25*215/230/2, iconAnchorY = 16
)
leaflet(city_data) %>% addTiles() %>% 
    addMarkers(lng = city_data$lng, lat = city_data$lat, 
               label = city_data$city, icon = star_icon)
```