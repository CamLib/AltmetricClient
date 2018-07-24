# run the commands in the set_global_variables.R script
# to load the required packages and set the file path to
# the set of data files you want to work with.

# load an articles master file

articles <- read_csv(str_c(data_files_path, '_master.csv'))

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

# Orders articles by count of member of public posters

arrange(articles, desc(poster_count_members_of_public)) %>%
  View()

ggplot(data = articles) + 
  geom_point(mapping = aes(x = print_publication_date, y = altmetric_score))

group_by(articles, type) %>%
  summarise(total = n()) %>%
  View()
