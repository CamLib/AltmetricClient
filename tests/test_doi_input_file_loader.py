from altmetric_client.doi_input import DOIInputFileLoader

class TestDOIInputReader:

    def setup_method(self):

        self._test_doi_loader = DOIInputFileLoader()

    def tear_down_method(self):

        self._test_doi_loader = None

    def test_add_input_file_path(self):

        self._test_doi_loader.input_file_path = 'test_input_file_path'
        assert self._test_doi_loader.input_file_path == 'test_input_file_path'

    def test_add_file_path_in_constructor(self):

        test_filepath_in_constructor = DOIInputFileLoader('test_file_path')
        assert test_filepath_in_constructor.input_file_path == 'test_file_path'

    def test_input_file_returns_lost_of_three_dois(self):

        self._test_doi_loader.input_file_path = '../files_in/test_input.csv'
        result = self._test_doi_loader.load_dois()
        assert len(result) == 3

    def test_first_doi_correct(self):

        self._test_doi_loader.input_file_path = '../files_in/test_input.csv'
        result = self._test_doi_loader.load_dois()
        assert result[0] == 'Test/doi_001'

    def test_third_doi_correct(self):

        self._test_doi_loader.input_file_path = '../files_in/test_input.csv'
        result = self._test_doi_loader.load_dois()

        assert result[2] == 'Test/doi_003'

    def test_file_not_found_error(self, capfd):

        '''This test uses Pytest's capfd fixture to check that the exception handling has printed out an error
        message when the input file can't be found. This works by passing a Pytest 'capfd' fixture to the test,
        then reading the output it captures and asserting it is as expected. More here:
        https://docs.pytest.org/en/2.9.1/capture.html'''

        self._test_doi_loader.input_file_path = 'file/does/not/exist.csv'
        result = self._test_doi_loader.load_dois()
        out, err = capfd.readouterr()
        assert out == 'Could not find the input file at the location: file/does/not/exist.csv\n'