import os


class CSVWriterBase:

    def __init__(self,
                 output_file_name=None,
                 output_directory_name=None):

        self._output_file_name = output_file_name
        self._output_directory_name = output_directory_name

    @property
    def output_file_name(self):
        return self._output_file_name

    @output_file_name.setter
    def output_file_name(self, output_file_name):
        self._output_file_name = output_file_name

    @property
    def output_directory_name(self):
        return self._output_directory_name

    @output_directory_name.setter
    def output_directory_name(self, output_directory_name):
        self._output_directory_name = output_directory_name

    def _get_write_mode(self, filepath):

        if os.path.isfile(filepath):
            return 'a'
        else:
            return 'w'
