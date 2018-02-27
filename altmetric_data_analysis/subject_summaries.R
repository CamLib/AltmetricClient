# run the commands in the set_global_variables.R script
# to load the required packages and set the file path to
# the set of data files you want to work with.

# load a subjects file

subjects <- read_csv(str_c(data_files_path, "_subjects.csv"))

# bar chart the altmetric subjects

(altmetric_subject_totals <- filter(subjects, subject_scheme == 'altmetric') %>%
    group_by(subject_name) %>%
    summarise(total = n()) %>%
    arrange(desc(total)))

altmetric_subject_totals %>%
  View()
                      
  
