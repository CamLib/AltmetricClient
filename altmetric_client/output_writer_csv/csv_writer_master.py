from altmetric_client.altmetric import Altmetric
from csv import DictWriter

class CSVWriterMaster:

    def __init__(self,\
                 output_file_name=None,\
                 output_directory_name=None,\
                 altmetric=None):

        self._ouput_file_name = output_file_name
        self._output_directory_name = output_directory_name
        self._altmetric = altmetric

    @property
    def output_file_name (self):
        return self._ouput_file_name

    @output_file_name.setter
    def output_file_name(self, output_file_name):
        self._ouput_file_name = output_file_name

    @property
    def output_directory_name(self):
        return self._output_directory_name

    @output_directory_name.setter
    def output_directory_name(self, output_directory_name):
        self._output_directory_name = output_directory_name

    @property
    def altmetric(self):
        return self._altmetric

    @altmetric.setter
    def altmetric(self, altmetric:Altmetric):
        self._altmetric = altmetric

    def write_master(self):

        output_file_path = '{0}{1}'.format(self.output_directory_name, self.output_file_name)

        fieldnames = ['altmetric_id']

        with open(output_file_path, 'w') as output_csv:

            output_writer = DictWriter(output_csv, fieldnames=fieldnames)
            output_writer.writeheader()
