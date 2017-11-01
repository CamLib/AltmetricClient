import configparser
import os

from altmetric_client.altmetric_api_config import AltmetricAPIConfig
from altmetric_client.output_writer_csv.csv_writer_master import CSVWriterMaster
from altmetric_client.url_builder import URLBuilder
from altmetric_client.altmetric_request import AltmetricRequest
from altmetric_client.altmetric_loader import AltmetricLoader
from altmetric_client.doi_input import DOIInputFileLoader

class TestIssue9:

    def setup_method(self):

        config_data = configparser.ConfigParser()

        self.files_out_directory = "../files_out/"
        self.test_output_file_name = "test_issue9results.csv"
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

    def test_doi_ends_with_61611_0(self):

        self._run_test_with_doi('10.1016/s0140-6736(12)61611-0')
        assert os.path.isfile(self.filepath)

    def test_doi_ends_with_10137_x(self):

        self._run_test_with_doi('10.1016/s0140-6736(98)10137-x')
        assert os.path.isfile(self.filepath)

    def test_doi_ends_with_15264(self):

        self._run_test_with_doi('10.1017/s0022143000015264')
        assert os.path.isfile(self.filepath)

    def test_doi_ends_with_p0048(self):

        self._run_test_with_doi('10.20965/jdr.2012.p0048')
        assert os.path.isfile(self.filepath)

    def test_doi_ends_with_166983(self):

        self._run_test_with_doi('10.1145/2166966.2166983')
        assert os.path.isfile(self.filepath)

    def test_doi_ends_with_45357(self):

        self._run_test_with_doi('10.1145/2145204.2145347')
        assert os.path.isfile(self.filepath)

    def test_doi_ends_with_017(self):

        self._run_test_with_doi('10.1016/j.econlet.2011.12.071')
        assert os.path.isfile(self.filepath)
