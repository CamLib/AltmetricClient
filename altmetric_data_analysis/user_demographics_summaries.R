# install.packages("tidyverse")

library(tidyverse)

# load a user demographics file

user_demographics <- read_csv("../files_out/20180130_0810_user_demographics.csv")

# filter by mendeley by_status - professor - then order by the most mentioned

filter(user_demographics, 
       demographic_source == 'mendeley', 
       demographic_group_type == 'by_status', 
       demographic_group_value == 'Professor') %>%
  arrange(desc(demographic_total)) %>%
  View()



