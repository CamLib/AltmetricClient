import configparser
import os

from altmetric_client.altmetric_api_config import AltmetricAPIConfig
from altmetric_client.output_writer_csv.csv_writer_master import CSVWriterMaster
from altmetric_client.url_builder import URLBuilder
from altmetric_client.altmetric_request import AltmetricRequest
from altmetric_client.altmetric_loader import AltmetricLoader

class TestIssue9:

    def setup_method(self):

        config_data = configparser.ConfigParser()

        self.files_out_directory = "../files_out/"
        self.test_output_file_name = "test_issue8results.csv"
        self.filepath = '{0}{1}'.format(self.files_out_directory, self.test_output_file_name)

        if os.path.isfile(self.filepath):
            os.remove(self.filepath)

        with open('../config.ini') as config_file:
            config_data.read_file(config_file)

        api_config = AltmetricAPIConfig()
        api_config.api_base_uri = config_data['api.altmetric.com']['APIBaseURI']
        api_config.api_version = config_data['api.altmetric.com']['APIVersion']
        api_config.api_base_command = config_data['api.altmetric.com']['APIBaseCommand']
        api_config.api_requested_item_id_type = config_data['api.altmetric.com']['APIRequestedItemIdType']
        api_config.api_key = config_data['api.altmetric.com']['APIKey']

        url_builder = URLBuilder(api_config)
        self.altmetric_request = AltmetricRequest(url_builder)
        self.altmetric_loader = AltmetricLoader()

        self.csv_writer = CSVWriterMaster(self.test_output_file_name, self.files_out_directory)

    def _run_test_with_doi(self, doi):

        self.altmetric_request.doi_to_request = doi
        altmetric_data = self.altmetric_request.request()
        altmetric = self.altmetric_loader.parse_result(altmetric_data)
        altmetric.doi = doi
        self.csv_writer.altmetric = altmetric
        self.csv_writer.write_master()

    def test_doi_ends_with_08_029(self):

        self._run_test_with_doi('10.1016/j.cell.2014.08.029')
        assert os.path.isfile(self.filepath)

    def test_doi_ends_with_09_033(self):

        self._run_test_with_doi('10.1016/j.socscimed.2012.09.033')
        assert os.path.isfile(self.filepath)

    def test_doi_ends_with_0366_6(self):

        self._run_test_with_doi('10.1007/s10113-012-0366-6')
        assert os.path.isfile(self.filepath)

    def test_doi_ends_with_12_071(self):

        self._run_test_with_doi('10.1016/j.econlet.2011.12.071')
        assert os.path.isfile(self.filepath)

    def test_doi_ends_with_ast051(self):

        self._run_test_with_doi('10.1093/biomet/ast051')
        assert os.path.isfile(self.filepath)
