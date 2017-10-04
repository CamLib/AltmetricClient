from csv import DictReader

class DOIInputFileLoader:

    def __init__(self, input_file_path=None):

        self.__input_file_path = input_file_path


    @property
    def input_file_path(self):

        return self.__input_file_path

    @input_file_path.setter
    def input_file_path(self, input_file_path):

        self.__input_file_path = input_file_path

    def load_dois(self):

        doi_list = []

        with open(self.input_file_path, 'r') as doi_input_csv:

            doi_input_reader = DictReader(doi_input_csv)

            for doi_row in doi_input_reader:

                doi_list.append(doi_row['DOI'])

        return doi_list