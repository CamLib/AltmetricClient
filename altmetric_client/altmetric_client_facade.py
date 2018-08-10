import sys

from altmetric_client.altmetric_api_config import AltmetricAPIConfig
from altmetric_client.output_writer_csv.csv_writer_facade import CSVWriterFacade
from altmetric_client.url_builder import URLBuilder
from altmetric_client.altmetric_request import AltmetricRequest
from altmetric_client.author_manager import AuthorManager
from altmetric_client.altmetric_loader import AltmetricLoader
from altmetric_client.doi_input import DOIInputFileLoader
from altmetric_client.json_file_manager import JSONFileManager

class AltmetricClientFacade:

    def __init__(self,
                 config:AltmetricAPIConfig=None,
                 files_in_directory:str=None,
                 input_file_name:str=None,
                 files_out_directory:str=None,
                 output_files_root:str=None,
                 behaviour:str=None):

        # this is where to set a behaviour (e.g. 'write csv', 'write something else', 'generate list'
        # at some point later on when the AltmetricClient supports multiple behaviours

        self._config = config
        self._files_in_directory = files_in_directory
        self._input_file_name = input_file_name
        self._files_out_directory = files_out_directory
        self._output_files_root = output_files_root
        self._behaviour = behaviour
        self._error_dois = []

    def execute(self):

        csv_writer = CSVWriterFacade(self._files_out_directory, self._output_files_root)
        url_builder = URLBuilder(self._config)
        altmetric_request = AltmetricRequest(url_builder)
        doi_loader = DOIInputFileLoader('{0}{1}'.format(self._files_in_directory,self._input_file_name))
        doi_list = doi_loader.load_dois()
        total_dois = len(doi_list)
        print('{0} DOIs loaded'.format(total_dois))
        author_manager = AuthorManager()
        altmetric_loader = AltmetricLoader()
        altmetric_loader.author_manager = author_manager
        json_file_manager = JSONFileManager(self._files_out_directory)
        total_retrieved = 1
        error_count = 0

        for doi in doi_list:

            altmetric_request.doi_to_request = doi

            try:

                if self._behaviour == "load":

                    altmetric_data = json_file_manager.load(self._files_in_directory, doi)

                else:

                    altmetric_data = altmetric_request.request()

                if self._behaviour == 'dump':

                    json_file_manager.dump(altmetric_data, doi)

                else:

                    altmetric = altmetric_loader.parse_result(altmetric_data)
                    csv_writer.write(altmetric)

                print('{0}/{1} DOIs retrieved'.format(total_retrieved, total_dois))
                total_retrieved += 1

            except:
                print('An error occurred when retrieving DOI {0}/{1} - {2}'.format(total_retrieved, total_dois, doi))
                print('The error was: '), sys.exc_info()[0]
                error_count += 1
                self._error_dois.append(doi)

        print('Retrieval of {0} DOIs completed with {1} errors'.format(total_dois, error_count))

        complete_author_list = altmetric_loader.authors_list

        print('An author list of {0} authors was extracted from the dataset. Writing these to a CSV'
              .format(len(complete_author_list)))

        csv_writer.write_authors(complete_author_list)

        if len(self._error_dois) > 0:

            print('The following DOIs caused errors:')

            for error_doi in self._error_dois:
                print(error_doi)

        print('All done. Have a nice day.')