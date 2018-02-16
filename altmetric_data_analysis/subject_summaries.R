# install.packages("tidyverse")

library(tidyverse)

# load a subjects file

subjects <- read_csv("../files_out/20180215_0938_subjects.csv")

# bar chart the altmetric subjects

(altmetric_subject_totals <- filter(subjects, subject_scheme == 'altmetric') %>%
    group_by(subject_name) %>%
    summarise(total = n()) %>%
    arrange(desc(total)))

altmetric_subject_totals %>%
  View()
                      
  
