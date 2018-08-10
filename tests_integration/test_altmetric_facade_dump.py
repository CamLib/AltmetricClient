import configparser
import os

from altmetric_client.altmetric_api_config import AltmetricAPIConfig
from altmetric_client.altmetric_client_facade import AltmetricClientFacade

class TestAltmetricFacadeDump:

    def setup_method(self):

        config_data = configparser.ConfigParser()

        # There's a relative path here, so the test will only run (in PyCharm) if the working directory
        # is set properly in the test run configuration.
        # See https://www.jetbrains.com/help/pycharm/run-debug-configuration.html

        with open('../config.ini') as config_file:
            config_data.read_file(config_file)

        self.api_config = self._load_config(config_data)

        _test_input_file_name = 'test_dois_minimum_end_to_end.csv'
        _files_in_directory = '../files_in/'
        _files_out_directory = "test_dump"

        self.test_altmetric_facade = AltmetricClientFacade(self.api_config,
                                                           _files_in_directory,
                                                           _test_input_file_name,
                                                           _files_out_directory,
                                                           None,
                                                           "dump")



    def tear_down_method(self):

        self._test_altmetric_request = None

    def _load_config(self, config_data):

        '''Loads the API config in the same way as the client app in the root directory, only
        (as befits a test), with none of the error handling.'''

        api_config = AltmetricAPIConfig()

        api_config.api_base_uri = config_data['api.altmetric.com']['APIBaseURI']
        api_config.api_version = config_data['api.altmetric.com']['APIVersion']
        api_config.api_base_command = config_data['api.altmetric.com']['APIBaseCommand']
        api_config.api_requested_item_id_type = config_data['api.altmetric.com']['APIRequestedItemIdType']
        api_config.api_key = config_data['api.altmetric.com']['APIKey']

        return api_config

