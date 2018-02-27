# run the commands in the set_global_variables.R script
# to load the required packages and set the file path to
# the set of data files you want to work with.

# load an articles master file

articles <- read_csv(str_c(data_files_path, "_master.csv"))

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
