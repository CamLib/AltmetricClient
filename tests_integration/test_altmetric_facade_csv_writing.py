import configparser
import os
from csv import DictReader

from altmetric_client.altmetric_api_config import AltmetricAPIConfig
from altmetric_client.altmetric_client_facade import AltmetricClientFacade

class TestAltmetricFacadeCSVWriting:

    '''Test class for the AltmetricClientFacade, which orchestrates all the parts of the AltmetricClient.
    This is another integration test put in a completely separate directory so that it's easier to exclude it
    from other test runs. Otherwise, simply running all the tests is going to hit the Altmetric endpoint all the time.
    
    This is also why the call to the facade functionality to get the data and write it to a CSV is in 
    a class setup - so the test only makes the call once, writes the results out, and then all the other tests
    read from the written-out CSV.
    
    Initially the facade only has one behaviour, which is to write out Altmetric data to CSV files. More end-to-end
    tests will need to be added as extra behaviours are added.

    As with all the integration tests, the configuration is also loaded from the project config, so that we 
    don't end up putting our API key in the codebase. :) ... 
    
    Running this test is a good way to check that you've got your config setup correctly.'''

    @classmethod
    def setup_class(cls):

        # Setup test file names and paths
        # Relative paths are used here, so the test will only run (in PyCharm) if the working directory
        # is set properly in the test run configuration.
        # See https://www.jetbrains.com/help/pycharm/run-debug-configuration.html

        _test_input_file_name = 'test_dois_minimum_end_to_end.csv'
        _files_in_directory = '../files_in/'

        _test_output_name_root = 'test_bare_minimum_end_to_end'
        _files_out_directory = '../files_out/'

        # Delete the pre-existing output file if it's there

        filepath = '{0}{1}'.format(_files_out_directory, _test_output_name_root)

        if os.path.isfile(filepath):
            os.remove(filepath)

        # Load the config from the project's config file. This is never pushed to GitHub,
        # so see the README about how to set one up

        config_data = configparser.ConfigParser()

        with open('../config.ini') as config_file:
            config_data.read_file(config_file)

        api_config = AltmetricAPIConfig()
        api_config.api_base_uri = config_data['api.altmetric.com']['APIBaseURI']
        api_config.api_version = config_data['api.altmetric.com']['APIVersion']
        api_config.api_base_command = config_data['api.altmetric.com']['APIBaseCommand']
        api_config.api_requested_item_id_type = config_data['api.altmetric.com']['APIRequestedItemIdType']
        api_config.api_key = config_data['api.altmetric.com']['APIKey']

        test_altmetric_facade = AltmetricClientFacade(api_config,
                                                        _files_in_directory,
                                                        _test_input_file_name,
                                                        _files_out_directory,
                                                        _test_output_name_root)

        test_altmetric_facade.execute()

    def setup_method(self):

        self._test_master_output_file_path = '../files_out/test_bare_minimum_end_to_end_master.csv'
        self._test_mentions_output_file_path = '../files_out/test_bare_minimum_end_to_end_mentions.csv'


    def test_csv_writing_end_to_end_writes_altmetric_id(self):

        with open(self._test_master_output_file_path) as test_output_csv:

            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['altmetric_id'] == '1270180'

    def test_csv_writing_end_to_end_writes_doi(self):

        with open(self._test_master_output_file_path) as test_output_csv:

            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['doi'] == '10.1001/jama.2013.950'

    def test_mentions_csv_contains_you_are_informed_tweet(self):

        with open(self._test_mentions_output_file_path) as test_output_csv:

            test_output_reader = DictReader(test_output_csv)

            for row in test_output_reader:

                if row['url'] == 'http://twitter.com/youareinformed/statuses/307101916456951811':

                    assert True
