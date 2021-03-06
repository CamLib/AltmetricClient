# run the commands in the set_global_variables.R script
# to load the required packages and set the file path to
# the set of data files you want to work with.

# load a scores file

scores <- read_csv(str_c(data_files_path, "_scores.csv"))

arrange(select(scores, doi, total, context_all_rank), 
        context_all_rank) %>%
  View()
