from altmetric_client.output_writer_csv.csv_writer_master import CSVWriterMaster
from altmetric_client.altmetric import Altmetric
from csv import DictReader
import os

class TestExtraMasterOutput:

    def setup_method(self):

        self._test_file_name = 'test_extra_master_file.csv'
        self._files_out_directory = '../files_out/'

        # clean up the old test file in the setup

        filepath = '{0}{1}'.format(self._files_out_directory, self._test_file_name)

        if os.path.isfile(filepath):
            os.remove(filepath)

        # Original bare-minimum set of properties

        self._test_altmetric = Altmetric()
        self._test_altmetric.doi = '10/test.doi'
        self._test_altmetric.altmetric_id = 1234
        self._test_altmetric.altmetric_score = 13
        self._test_altmetric.article_title = 'Test Article Title'
        self._test_altmetric.journal_title = 'Test Journal Title'
        self._test_altmetric.altmetric_journal_id = 'Test Altmetric Journal Id'
        self._test_altmetric.total_mentions = 78
        self._test_altmetric.print_publication_date = '2013-02-27T00:00:00+00:00'
        self._test_altmetric.first_seen_on_date = '2014-03-15T00:00:00+00:00'
        self._test_altmetric.first_author = 'Test Author 1'

        # Extra master properties to be tested here

        self._test_altmetric.page_starts = "20"
        self._test_altmetric.page_ends = "30"
        self._test_altmetric.journal_volume = "5"
        self._test_altmetric.journal_issue = "2"
        self._test_altmetric.publisher = 'Test publisher'
        self._test_altmetric.last_mentioned_date = "1972-15-03T08:30"
        self._test_altmetric.pdf_url = 'http://test.com/pdf_url.pdf'
        self._test_altmetric.type = 'Test type'
        self._test_altmetric.uri = 'http://testuri.com'
        self._test_altmetric.mendeley_url = 'http://mendeley.com/testurl'
        self._test_altmetric.poster_type_members_of_public_count = 101
        self._test_altmetric.poster_type_researcher_count = 102
        self._test_altmetric.poster_type_practitioner_count = 103
        self._test_altmetric.poster_type_science_communicator_count = 104

        self.test_csv_writer_master = CSVWriterMaster(self._test_file_name, self._files_out_directory, self._test_altmetric)

    def tear_down_method(self):

        self.test_csv_writer_master = None


    def test_page_starts_added(self):

        self.test_csv_writer_master.write_master()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:

            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['page_starts'] == '20'

    def test_page_ends_added(self):

        self.test_csv_writer_master.write_master()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:

            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['page_ends'] == '30'

    def test_journal_volume_added(self):

        self.test_csv_writer_master.write_master()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:

            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['journal_volume'] == "5"

    def test_journal_issue_added(self):

        self.test_csv_writer_master.write_master()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:

            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['journal_issue'] == "2"

    def test_last_mentioned_date_added(self):

        self.test_csv_writer_master.write_master()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:

            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['last_mentioned_date'] == "1972-15-03T08:30"

    def test_pdf_url_added(self):

        self.test_csv_writer_master.write_master()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:

            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['pdf_url'] == "http://test.com/pdf_url.pdf"

    def test_publisher_added(self):

        self.test_csv_writer_master.write_master()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:

            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['publisher'] == "Test publisher"

    def test_type_added(self):

        self.test_csv_writer_master.write_master()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:

            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['type'] == "Test type"

    def test_uri_added(self):

        self.test_csv_writer_master.write_master()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:

            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['uri'] == "http://testuri.com"

    def test_mendeley_url_added(self):

        self.test_csv_writer_master.write_master()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:

            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['mendeley_url'] == "http://mendeley.com/testurl"

    def test_poster_type_members_of_public_count_added(self):

        self.test_csv_writer_master.write_master()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:

            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['poster_count_members_of_public'] == "101"

    def test_poster_type_researcher_count_added(self):

        self.test_csv_writer_master.write_master()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:

            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['poster_count_researcher'] == "102"

    def test_poster_type_practitioner_count_added(self):

        self.test_csv_writer_master.write_master()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:

            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['poster_count_practitioner'] == "103"

    def test_poster_type_science_communicator_count_added(self):

        self.test_csv_writer_master.write_master()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:

            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['poster_count_science_communicator'] == "104"
