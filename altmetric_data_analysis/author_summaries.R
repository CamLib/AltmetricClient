# install.packages("tidyverse")

library(tidyverse)

# load an authors file

authors <- read_csv("../files_out/20180118_0733_authors.csv")
mentions <- read_csv("../files_out/20180118_0733_mentions.csv")
articles <- read_csv("../files_out/20180118_0733_master.csv")

# articles %>% View()
# mentions %>% View()
# authors %>% View()

# Join mentions back to authors and write out for Lauren

# mentions %>%
#  left_join(authors) %>%
#  write_csv("../files_out/20171205_0734_mentions_with_authors.csv")

# mentions_with_authors <- read_csv("../files_out/20171205_0734_mentions_with_authors.csv")
# mentions_with_authors %>%
#  arrange(desc(author_follower_count)) %>%
#  View()

# who's got the most followers?

filter(authors, author_follower_count > 100000) %>%
arrange(desc(author_follower_count)) %>%
  View()

# which article has Neil Gaiman been Tweeting about?

all_data <- authors %>%
  left_join(mentions) %>%
  left_join(articles, by = c("related_article_doi" = "doi"))

filter(all_data, author_name == 'Neil Gaiman') %>%
  View()

# I guessed correctly!
  
# TODO: why are there less by a couple of hundred?

# Arrange articles by the total number of followers of the
# people that mention them

article_groups <- group_by(all_data, altmetric_id)
follower_totals <- summarise(article_groups, total_followers = sum(author_follower_count)) %>%
  arrange(desc(total_followers))

# Arrange articles by the total number of news mentions

news_totals <- filter(all_data, source == 'news') %>%
  count(altmetric_id)

# Join the two and plot any correlation between news articles and total mentions
# I'm pretty sure there's a more elegant way to do this from the originally-joined set
# using mutate - but I haven't worked it out yet

followers_and_news <- follower_totals %>%
  left_join(news_totals)

# Swap NAs for zeros (not sure if this makes a difference but it feels right and proper)

followers_and_news[is.na(followers_and_news)] <- 0

followers_and_news %>% 
  arrange(desc(n)) %>%
  View()

ggplot(data = followers_and_news) +
  geom_point(mapping = aes(x = total_followers, y = n))



