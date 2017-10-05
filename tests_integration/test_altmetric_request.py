from altmetric_client.altmetric_request import AltmetricRequest
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
    config setup correctly.
    '''

    def setup_method(self):

        self._test_altmetric_request