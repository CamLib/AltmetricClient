from altmetric_client.altmetric_api_config import AltmetricAPIConfig
from altmetric_client.output_writer_csv.csv_writer_master import CSVWriterMaster
from altmetric_client.url_builder import URLBuilder
from altmetric_client.altmetric_request import AltmetricRequest
from altmetric_client.altmetric_loader import AltmetricLoader
from altmetric_client.doi_input import DOIInputFileLoader

class AltmetricClientFacade:

    def __init__(self,
                 config:AltmetricAPIConfig=None,
                 files_in_directory:str=None,
                 input_file_name:str=None,
                 files_out_directory:str=None,
                 output_file_name:str=None):

        # this is where to set a behaviour (e.g. 'write csv', 'write something else', 'generate list'
        # at some point later on when the AltmetricClient supports multiple behaviours

        self._config = config
        self._files_in_directory = files_in_directory
        self._input_file_name = input_file_name
        self._files_out_directory = files_out_directory
        self._output_file_name = output_file_name

    def execute(self):

        csv_writer = CSVWriterMaster(self._output_file_name, self._files_out_directory)
        url_builder = URLBuilder(self._config)
        altmetric_request = AltmetricRequest(url_builder)
        doi_loader = DOIInputFileLoader('{0}{1}'.format(self._files_in_directory,self._input_file_name))
        doi_list = doi_loader.load_dois()
        altmetric_loader = AltmetricLoader()

        for doi in doi_list:

            altmetric_request.doi_to_request = doi
            altmetric_data = altmetric_request.request()
            csv_writer.altmetric = altmetric_loader.parse_result(altmetric_data)
            csv_writer.write_master()
