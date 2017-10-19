from altmetric_client.output_writer_csv.csv_writer_master import CSVWriterMaster
from altmetric_client.altmetric import Altmetric
from csv import DictReader
import os


class TestBareMinimumMasterOutput:

    def setup_method(self):

        self._test_file_name = 'test_bare_minimum_master_file.csv'
        self._files_out_directory = '../files_out/'

        # clean up the old test file in the setup

        filepath = '{0}{1}'.format(self._files_out_directory, self._test_file_name)

        if os.path.isfile(filepath):
            os.remove(filepath)

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
        self._test_altmetric.first_author = 'Test Author 1, Test Author 2'

        self.test_csv_writer_master = CSVWriterMaster(self._test_file_name, self._files_out_directory, self._test_altmetric)

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

    def test_file_created_with_header_containing_doi(self):

        self.test_csv_writer_master.write_master()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:

            test_output_reader = DictReader(test_output_csv)
            assert test_output_reader.fieldnames[0] == 'doi'

    def test_doi_added_to_master(self):
        self.test_csv_writer_master.write_master()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['doi'] == '10/test.doi'

    def test_altmetric_id_added_to_master(self):

        self.test_csv_writer_master.write_master()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:

            test_output_reader = DictReader(test_output_csv)

            assert int(next(test_output_reader)['altmetric_id']) == 1234

    def test_altmetric_score_added_to_master(self):

        self.test_csv_writer_master.write_master()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:

            test_output_reader = DictReader(test_output_csv)

            assert int(next(test_output_reader)['altmetric_score']) == 13

    def test_article_title_added_to_master(self):

        self.test_csv_writer_master.write_master()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['article_title'] == 'Test Article Title'

    def test_journal_title_added_to_master(self):

        self.test_csv_writer_master.write_master()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['journal_title'] == 'Test Journal Title'

    def test_altmetric_journal_id_added_to_master(self):

        self.test_csv_writer_master.write_master()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['altmetric_journal_id'] == 'Test Altmetric Journal Id'

    def test_total_mentions_added_to_master(self):

        self.test_csv_writer_master.write_master()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert int(next(test_output_reader)['total_mentions']) == 78

    def test_print_publication_date_added_to_master(self):

        self.test_csv_writer_master.write_master()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['print_publication_date'] == '2013-02-27T00:00:00+00:00'

    def test_first_seen_on_date_added_to_master(self):

        self.test_csv_writer_master.write_master()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['first_seen_on_date'] == '2014-03-15T00:00:00+00:00'

    def test_authors_added_to_master(self):

        self.test_csv_writer_master.write_master()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['authors'] == 'Test Author 1, Test Author 2'

    def test_new_article_info_appended_to_existing_file(self):

        # Write the first piece of data
        self.test_csv_writer_master.write_master()
        # Setup a second piece of data
        second_altmetric = Altmetric()
        second_altmetric.altmetric_id = 999
        self.test_csv_writer_master.altmetric = second_altmetric
        # Write the second piece
        self.test_csv_writer_master.write_master()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)
            # skip the first line to find the new piece of data
            next(test_output_reader)

            assert int(next(test_output_reader)['altmetric_id']) == 999

    def test_error_handled_if_filename_not_set(self, capfd):

        test_filenameless_csv_master_writer = CSVWriterMaster()
        test_filenameless_csv_master_writer.write_master()
        out, err = capfd.readouterr()
        assert out == 'Could not write a master csv file because the filename was not set in the Master CSV Writer\n'

    def test_error_handled_if_directory_not_set(self, capfd):

        test_directoryless_csv_master_writer = CSVWriterMaster()
        test_directoryless_csv_master_writer.output_file_name = 'FileNameSet.csv'
        test_directoryless_csv_master_writer.write_master()
        out, err = capfd.readouterr()
        assert out == 'Could not write a master csv file because the output directory was not set in the Master CSV Writer\n'

    def test_error_handled_if_altmetric_not_set(self, capfd):

        test_altmetricless_csv_master_writer = CSVWriterMaster()
        test_altmetricless_csv_master_writer.output_file_name = 'FileNameSet.csv'
        test_altmetricless_csv_master_writer.output_directory_name = 'DirectoryNameSet.csv'
        test_altmetricless_csv_master_writer.write_master()
        out, err = capfd.readouterr()
        assert out == 'Could not write a master csv file because the Altmetric data was not set in the Master CSV Writer\n'
