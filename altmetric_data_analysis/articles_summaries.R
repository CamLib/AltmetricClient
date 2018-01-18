# install.packages("tidyverse")

library(tidyverse)

# load an articles master file

articles <- read_csv("../files_out/20180118_0733_master.csv")

# Orders articles by total_mentions descending

arrange(select(articles, 
               doi, 
               total_mentions,
               article_title,
               first_author), 
        desc(total_mentions)) %>%
  View()

# Calculates the mean average total mentions

summarise(articles, mean(total_mentions))

# Calculates the interquartile range of the total mentions

summarise(articles, IQR(total_mentions))

# Returns articles with a certain number of mentions

filter(articles, total_mentions == 10) %>% 
  arrange(desc(total_mentions)) %>% 
  View()
