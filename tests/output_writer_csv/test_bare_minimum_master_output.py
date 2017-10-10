from altmetric_client.output_writer_csv.csv_writer_master import CSVWriterMaster
from altmetric_client.altmetric import Altmetric
from csv import DictReader

class TestBareMinimumMasterOutput:

    def setup_method(self):

        self._test_file_name = 'test_bare_minimum_master_file.csv'
        self._files_out_directory = '../files_out/'

        self._test_altmetric = Altmetric()
        self._test_altmetric.altmetric_id = 1234
        self._test_altmetric.altmetric_score = 13
        self._test_altmetric.article_title = 'Test Article Title'

        self.test_csv_writer_master = CSVWriterMaster(self._test_file_name, self._files_out_directory)

    def tear_down_method(self):

        self.test_csv_writer_master = None

    def test_file_name_added(self):

        self.test_csv_writer_master.output_file_name = 'Test Output File Name'
        assert 'Test Output File Name' == self.test_csv_writer_master.output_file_name

    def test_directory_name_added(self):

        self.test_csv_writer_master.output_directory_name = 'Test Output Dir Name'
        assert 'Test Output Dir Name' == self.test_csv_writer_master.output_directory_name

    def test_altmetric_object_added(self):

        test_altmetric = Altmetric()
        test_altmetric.altmetric_id = 1234
        self.test_csv_writer_master.altmetric = test_altmetric
        assert self.test_csv_writer_master.altmetric.altmetric_id == 1234

    def test_file_created_with_header_containing_altmetric_id(self):

        self.test_csv_writer_master.altmetric = self._test_altmetric
        self.test_csv_writer_master.write_master()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:

            test_output_reader = DictReader(test_output_csv)
            assert test_output_reader.fieldnames[0] == 'altmetric_id'

    # Test altmetric_id is added to brand new file

    # Test altmetric_score

    # Test article_title

    # Test journal_title

    # Test altmetric_journal_id

    # Test total_mentions

    # Test print_publication_date

    # Test first_seen_on_date

    # Test authors

    # Test existing file is appended to with a new set of data

    # Test error thrown if file name not set

    # Test error thrown if directory not set

    # Test error thrown if altmetric not set