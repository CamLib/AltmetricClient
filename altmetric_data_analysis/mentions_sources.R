# install.packages("tidyverse")

library(tidyverse)

# load a mentions file

mentions <- read_csv("../files_out/20171122_0807_mentions.csv")

# Basic plot of the sources in a bar chart

ggplot(data = mentions) +
  geom_bar(mapping = aes(x = source)) +
  coord_flip()

# Puts a view on mentions filtered by source

filter(mentions, source == 'linkedin') %>%
  View()

# TODO Plot a histogram / freq_poly of tweet freqencies
# TODO Facets of mention frequency per article for different channels... (this will be hard as Twitter stomps on everything)
# TODO Facets of tweet frequency for a subset of similar papers (maybe)?

