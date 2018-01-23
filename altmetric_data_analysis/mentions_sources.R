# install.packages("tidyverse")

library(tidyverse)

# load a mentions file

mentions <- read_csv("../files_out/20180118_0733_mentions.csv")
articles <- read_csv("../files_out/20180118_0733_master.csv")

# Basic plot of the sources in a bar chart

ggplot(data = mentions) +
  geom_bar(mapping = aes(x = source)) +
  coord_flip()

# Puts a view on mentions filtered by source

filter(mentions, source == 'linkedin') %>%
  View()

# Plots a freqpoly of tweet freqencies for the whole set, by week

filter(mentions, source == 'twitter') %>%
  ggplot(aes(date_posted)) +
         geom_freqpoly(binwidth = 604800)
  
# Mention frequency (per day) for a specific article
# facetted across different channels, with Twitter 
# filtered out as it stomps on everything.
# 10.1136/bmj.g3725 is the most mentioned article.

filter(mentions, related_article_doi == '10.1136/bmj.g3725' & source != 'twitter') %>%
  ggplot(aes(date_posted)) +
  geom_freqpoly(binwidth = 86400) +
  facet_wrap(~ source)

# Join the two datasets.
# Refactored to name the joining variable 'doi' across the join

articles_with_mentions <- articles %>% 
  left_join(mentions)

articles_with_mentions %>% View()

# Facets tweet frequency for a subset of similar papers
# There are 9 articles in the set with a similar number of mentions 
# (20 either side of the average) all published in 2014


average_articles <- filter(articles_with_mentions,  +
                             between(total_mentions, 70, 110) & + 
                             print_publication_date > "2014-01-01" & +
                             print_publication_date < "2014-12-31")

# Facets a freqpoly of mention freqencies for the average articles

ggplot(data = average_articles, mapping = aes(x = date_posted)) +
  geom_freqpoly(binwidth = 604800) +
  facet_wrap(~ doi)
