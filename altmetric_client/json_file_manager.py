import json
import os

class JSONFileManager:

    def __init__(self, output_directory_path):

        self.__output_directory_path = output_directory_path

    def dump(self, data, doi:str):

        output_file_path = "{0}{1}.json".format(self.__output_directory_path, doi.replace("/", "---"))

        try:

            with open(output_file_path, 'w') as write_file:

                json.dump(data, write_file)

        except:

            print('Could not dump the JSON file for Altmetric with DOI: {0}'.format(doi))

    def load(self, input_directory:str, doi:str):

        try:

            input_file_path = "{0}/{1}.json".format(input_directory, doi.replace("/", "---"))

            with open(input_file_path, 'r') as json_file:

                return json.load(json_file)

        except Exception as ex:

            print('Could not load JSON file from filepath {0}'.format(filepath))
            print(ex)

