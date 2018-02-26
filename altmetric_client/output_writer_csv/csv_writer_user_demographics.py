from csv import DictWriter
from altmetric_client.output_writer_csv.csv_writer_base import CSVWriterBase

class CSVWriterUserDemographics(CSVWriterBase):

    def __init__(self,
                 output_file_name=None,
                 output_directory_name=None,
                 user_demographics_list=None):

        CSVWriterBase.__init__(self, output_file_name, output_directory_name)
        self.__user_demographics_list = user_demographics_list

    @property
    def user_demographics_list(self):
        return self.__user_demographics_list

    @user_demographics_list.setter
    def user_demographics_list(self, user_demographics_list):
        self.__user_demographics_list = user_demographics_list


    def write_user_demographics(self):

        output_file_path = '{0}{1}'.format(self.output_directory_name, self.output_file_name)

        write_mode = self._get_write_mode(output_file_path)

        fieldnames = ['doi', 'demographic_source', 'demographic_group_type',
                      'demographic_group_value', 'demographic_total']

        try:

            with open(output_file_path, write_mode) as output_csv:

                output_writer = DictWriter(output_csv, fieldnames=fieldnames)

                if write_mode == 'w':

                    output_writer.writeheader()

                for user_demographics in self.__user_demographics_list:

                    output_dict = dict(doi=user_demographics.doi,
                                       demographic_source=user_demographics.source,
                                       demographic_group_type=user_demographics.group_type,
                                       demographic_group_value=user_demographics.group_value,
                                       demographic_total=user_demographics.total)

                    output_writer.writerow(output_dict)

        except:

            print('Something totally unexpected happened when trying to write to a User Demographics CSV file')
            print('The writer was setup to write to a file called {0}{1}'.format(self.output_directory_name,
                                                                                 self.output_file_name))
            if write_mode == 'a':
                print('The writer thought this file existed and was trying to append to it.')
            elif write_mode == 'w':

                print('The writer thought this was a brand new file and was trying to create it.')
            else:
                print('The writer could not determine whether or not the file existed.')