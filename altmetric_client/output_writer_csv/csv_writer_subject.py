from csv import DictWriter
from altmetric_client.output_writer_csv.csv_writer_base import CSVWriterBase

class CSVWriterSubject(CSVWriterBase):

    def __init__(self,
                 output_file_name=None,
                 output_directory_name=None,
                 subjects_list=None):

        CSVWriterBase.__init__(self, output_file_name, output_directory_name)
        self.__subjects_list = subjects_list

    @property
    def subjects_list(self):
        return self.__subjects_list

    @subjects_list.setter
    def subjects_list(self, subjects_list):
        self.__subjects_list = subjects_list

    def write_subjects(self):

        output_file_path = '{0}{1}'.format(self.output_directory_name, self.output_file_name)

        write_mode = self._get_write_mode(output_file_path)

        fieldnames = ['doi', 'subject_scheme', 'subject_name']

        try:

            with open(output_file_path, write_mode) as output_csv:

                output_writer = DictWriter(output_csv, fieldnames=fieldnames)

                if write_mode == 'w':
                    output_writer.writeheader()

                for subject in self.__subjects_list:

                    output_dict = dict(doi=subject.doi,
                                       subject_scheme=subject.scheme,
                                       subject_name=subject.name)

                    output_writer.writerow(output_dict)

        except:

            print('Something totally unexpected happened when trying to write to a Subjects CSV file')
            print('The writer was setup to write to a file called {0}{1}'.format(self.output_directory_name,
                                                                                 self.output_file_name))
            if write_mode == 'a':
                print('The writer thought this file existed and was trying to append to it.')
            elif write_mode == 'w':

                print('The writer thought this was a brand new file and was trying to create it.')
            else:
                print('The writer could not determine whether or not the file existed.')
