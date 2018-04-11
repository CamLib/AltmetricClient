import sys
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

        try:

            with open(self.input_file_path, 'r') as doi_input_csv:

                doi_input_reader = DictReader(doi_input_csv)

                for doi_row in doi_input_reader:

                    doi_list.append(doi_row['DOI'])

        except FileNotFoundError:

            print("Could not find the input file at the location: {0}".format(self.input_file_path))

        except Exception as ex:

            print("The input file was found OK, but something weird happened when loading it.")
            print('The error was: {0}'.format(ex))

        return doi_list