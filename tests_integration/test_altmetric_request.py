import configparser
from altmetric_client.altmetric_request import AltmetricRequest
from altmetric_client.altmetric_api_config import AltmetricAPIConfig
from altmetric_client.url_builder import URLBuilder


class TestAlmetricRequest:

    '''Test class for the object that calls the Altmetric API.
    These tests have been put in a completely separate directory so that it's easier to exclude them
    from other test runs. Otherwise, simply running all the tests is going to hit the Altmetric endpoint all the time.
    The tests only check a couple of the aspects of the returned JSON that aren't going to change. There are other tests
    using locally-stored JSON (which also won't change) in the Unit Tests in the main tests folder, which actually test
    the full JSON-parsing code base.
    
    All the configuration is also loaded from the project config in this integration test, too, so that we don't end up
    putting our API key in the codebase. :) ... so running this test is also a good way to check that you've got your
    config setup correctly.'''

    def setup_method(self):

        # Load the config from the project's config file. This is never pushed to GitHub,
        # so see the README about how to set one up

        config_data = configparser.ConfigParser()

        # There's a relative path here, so the test will only run (in PyCharm) if the working directory
        # is set properly in the test run configuration.
        # See https://www.jetbrains.com/help/pycharm/run-debug-configuration.html

        with open('../config.ini') as config_file:
            config_data.read_file(config_file)

        self.api_config = self._load_config(config_data)

        # Load most of the config (other than the DOI) into a URLBuilder

        url_builder = self._configure_url_builder(self.api_config)
        self._test_altmetric_request = AltmetricRequest(url_builder)

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

    def _configure_url_builder(self, config_data):

        url_builder = URLBuilder(config_data)
        url_builder.build_url()
        return url_builder

    def test_data_returned_when_config_valid(self):

        '''This test uses the specific article DOI I was given to test with. This means that, if Altmetric use
        'API hits for DOIs' in any of their popularity measures, this article could get very popular quite
        quickly, for no good reason... This is one of the reasons why integration tests have been split off
        from the local Unit tests in the main test folder.

        TODO: Switch this to one of my own papers ASAP. :)'''

        self._test_altmetric_request.doi_to_request = '10.1001/jama.2013.950'
        result = self._test_altmetric_request.request()

        assert 'Surveillance Intervals for Small Abdominal Aortic Aneurysms: A Meta-analysis' == result["citation"]["title"]

    def test_error_printed_when_doi_not_set(self, capfd):

        result = self._test_altmetric_request.request()
        out, err = capfd.readouterr()
        assert out == 'A request to the Altmetric API was made without setting a DOI.\n'

    def test_error_printed_when_config_not_set(self, capfd):

        self._test_altmetric_request.url_builder = None
        self._test_altmetric_request.doi_to_request = 'Test DOI'
        result = self._test_altmetric_request.request()
        out, err = capfd.readouterr()
        assert out == 'A request to the Altmetric API was made without loading the config settings.\n'

    def test_requesting_with_invalid_key_prints_correct_error(self, capfd):

        self.api_config.api_key = 'Busted_Key'
        broken_key = URLBuilder(self.api_config)
        self._test_altmetric_request.url_builder = broken_key
        self._test_altmetric_request.doi_to_request = '10.1001/jama.2013.950'
        result = self._test_altmetric_request.request()
        out, err = capfd.readouterr()
        assert out == 'Altmetric have denied access for the request for DOI 10.1001/jama.2013.950. The wrong API key may have been used in the configuration?\n'

    # Test - requesting with the wrong config throws a 404 of some sort

    def test_requesting_with_misconfiguration_prints_correct_error(self, capfd):

        self.api_config.api_base_command = 'broken'
        broken_url = URLBuilder(self.api_config)
        self._test_altmetric_request.url_builder = broken_url
        self._test_altmetric_request.doi_to_request = '10.1001/jama.2013.950'
        result = self._test_altmetric_request.request()
        out, err = capfd.readouterr()
        assert out == 'Altmetric have returned a 404 error for the request. This is most likely because of an error in your config file.\n'
