# install.packages("tidyverse")

library(tidyverse)

# load a mentions file

mentions <- read_csv("../files_out/20171122_0807_mentions.csv")

ggplot(data = mentions) +
  geom_bar(mapping = aes(x = source)) +
  coord_flip()
