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
