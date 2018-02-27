# run the commands in the set_global_variables.R script
# to load the required packages and set the file path to
# the set of data files you want to work with.

# load a user demographics file

user_demographics <- read_csv(str_c(data_files_path, "_user_demographics.csv"))

# filter by mendeley by_status - professor - then order by the most mentioned

filter(user_demographics, 
       demographic_source == 'mendeley', 
       demographic_group_type == 'by_status', 
       demographic_group_value == 'Professor') %>%
  arrange(desc(demographic_total)) %>%
  View()



