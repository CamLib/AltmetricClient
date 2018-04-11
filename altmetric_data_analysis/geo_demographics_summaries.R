# run the commands in the set_global_variables.R script
# to load the required packages and set the file path to
# the set of data files you want to work with.

# load a geo demographics file

geo_demographics <- read_csv(str_c(data_files_path, "_geo_demographics.csv"))

# Find totals of the twitter geo demographics by country code

filter(geo_demographics, geo_demographic_source == 'twitter') %>%
    group_by(country_code) %>%
    summarise(total = sum(geo_demographic_total)) %>%
    arrange(desc(total)) %>%
    View()
