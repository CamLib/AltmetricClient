from altmetric_client.url_builder import URLBuilder
from altmetric_client.altmetric_api_config import AltmetricAPIConfig

class TestURLBuilder:

    def setup_method(self):

        self._test_url_builder = URLBuilder()

    def teardown_method(self):

        self._test_url_builder = None

    def test_base_url_added(self):

        altmetric_api_config = AltmetricAPIConfig()
        altmetric_api_config.api_base_uri = "http://api.test.value"

        self._test_url_builder.altmetric_api_config = altmetric_api_config

        assert self._test_url_builder.build_url() == 'http://api.test.value'

    def test_api_version_added(self):

        altmetric_api_config = AltmetricAPIConfig()
        altmetric_api_config.api_version = "vTest"

        self._test_url_builder.altmetric_api_config = altmetric_api_config

        assert self._test_url_builder.build_url() == '/vTest'

    def test_api_base_command_added(self):

        altmetric_api_config = AltmetricAPIConfig()
        altmetric_api_config.api_base_command = "testBaseCommand"

        self._test_url_builder.altmetric_api_config = altmetric_api_config

        assert self._test_url_builder.build_url() == '/testBaseCommand'

    def test_api_requested_item_type_added(self):

        altmetric_api_config = AltmetricAPIConfig()
        altmetric_api_config.api_requested_item_id_type = "testRequestedItemType"

        self._test_url_builder.altmetric_api_config = altmetric_api_config

        assert self._test_url_builder.build_url() == '/testRequestedItemType'

    def test_api_key_added(self):

        altmetric_api_config = AltmetricAPIConfig()
        altmetric_api_config.api_key = "testKey"

        self._test_url_builder.altmetric_api_config = altmetric_api_config

        assert self._test_url_builder.build_url() == '?key=testKey'

    def test_config_added_to_url(self):

        altmetric_api_config = AltmetricAPIConfig()
        altmetric_api_config.api_base_uri = 'http://test.base.uri'
        altmetric_api_config.api_version = 'testVersion'
        altmetric_api_config.api_base_command = 'testBaseCommand'
        altmetric_api_config.api_requested_item_id_type = 'testRequestedItemType'
        altmetric_api_config.api_key = 'testKey'

        self._test_url_builder.altmetric_api_config = altmetric_api_config

        assert self._test_url_builder.build_url() == 'http://test.base.uri/testVersion/testBaseCommand' \
                                                     '/testRequestedItemType?key=testKey'


    def test_doi_added_to_url(self):

        altmetric_api_config = AltmetricAPIConfig()
        self._test_url_builder.altmetric_api_config = altmetric_api_config

        self._test_url_builder.doi = 'test/doi12345'

        assert self._test_url_builder.build_url() == '/test/doi12345'

    def test_entire_url_built(self):

        altmetric_api_config = AltmetricAPIConfig()
        altmetric_api_config.api_base_uri = 'http://test.base.uri'
        altmetric_api_config.api_version = 'testVersion'
        altmetric_api_config.api_base_command = 'testBaseCommand'
        altmetric_api_config.api_requested_item_id_type = 'testRequestedItemType'
        altmetric_api_config.api_key = 'testKey'

        self._test_url_builder.altmetric_api_config = altmetric_api_config

        self._test_url_builder.doi = 'test/doi12345'

        assert self._test_url_builder.build_url() == 'http://test.base.uri/testVersion/testBaseCommand' \
                                                     '/testRequestedItemType/test/doi12345?key=testKey'