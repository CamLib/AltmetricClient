# install.packages("tidyverse")

library(tidyverse)

# load an articles master file

articles <- read_csv("../files_out/20171107_Master_BareMinimum.csv")

# plots articles by publication date and total mentions

ggplot(articles, aes(x = print_publication_date, y = total_mentions)) +
  geom_point() 

# plots a trend line through the mentions by date

ggplot(articles, aes(x = print_publication_date, y = total_mentions)) +
  geom_smooth()

# plots the articles and the trend on the same chart
# outlying articles with > 500 mentions excluded

ggplot(articles, aes(x = print_publication_date, y = total_mentions)) +
  geom_point() +
  geom_smooth() +
  coord_cartesian(ylim = c(0, 500))
