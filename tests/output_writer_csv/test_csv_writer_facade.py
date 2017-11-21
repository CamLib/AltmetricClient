import os
from csv import DictReader

from altmetric_client.output_writer_csv.csv_writer_facade import CSVWriterFacade
from altmetric_client.altmetric import Altmetric
from altmetric_client.mention import Mention

class TestCSVWriterFacade:

    def setup_method(self):

        test_file_root = 'test_csv_facade'
        output_directory_name = '../files_out/'

        self.master_filepath = '{0}{1}_master.csv'.format(output_directory_name, test_file_root)
        self.mentions_filepath = '{0}{1}_mentions.csv'.format(output_directory_name, test_file_root)

        # clean up the old test files in the setup

        if os.path.isfile(self.master_filepath):
            os.remove(self.master_filepath)

        if os.path.isfile(self.mentions_filepath):
            os.remove(self.mentions_filepath)

        test_altmetric = Altmetric()
        test_altmetric.altmetric_id = 1234
        test_altmetric.doi = "/Test/DOI/1234"

        test_mention = Mention()
        test_mention.related_article_doi = "/Test/DOI/1234"
        test_mention.url = "http://testurl1.com"

        test_altmetric.add_mention(test_mention)

        self.test_csv_writer_facade = CSVWriterFacade(output_directory_name, test_file_root)
        self.test_csv_writer_facade.write(test_altmetric)

    def teardown_method(self):

        self.test_csv_writer_facade = None

    def test_output_directory_name_set(self):

        assert self.test_csv_writer_facade.output_directory_name == '../files_out/'

    def test_output_file_root_set(self):

        assert self.test_csv_writer_facade.output_files_root == 'test_csv_facade'

    def test_altmetric_id_written_to_master(self):

        with open(self.master_filepath) as test_master_output_csv:

            test_output_reader = DictReader(test_master_output_csv)
            assert int(next(test_output_reader)['altmetric_id']) == 1234

    def test_url_written_to_mentions(self):

        with open(self.mentions_filepath) as test_mentions_output_csv:

            test_output_reader = DictReader(test_mentions_output_csv)
            assert next(test_output_reader)['url'] == 'http://testurl1.com'

    def test_second_altmetric_written_to_master(self):

        second_altmetric = Altmetric()
        second_altmetric.altmetric_id = 9876

        self.test_csv_writer_facade.write(second_altmetric)

        with open(self.master_filepath) as test_master_output_csv:

            test_output_reader = DictReader(test_master_output_csv)
            next(test_output_reader)
            assert int(next(test_output_reader)['altmetric_id']) == 9876

    def test_mention_from_second_altmetric_written_to_master(self):

        second_altmetric = Altmetric()
        second_altmetric.altmetric_id = 9876

        second_mention = Mention()
        second_mention.url = 'http://testurl2.com'

        second_altmetric.add_mention(second_mention)

        self.test_csv_writer_facade.write(second_altmetric)

        with open(self.mentions_filepath) as test_mentions_output_csv:
            test_output_reader = DictReader(test_mentions_output_csv)
            next(test_output_reader)
            assert next(test_output_reader)['url'] == 'http://testurl2.com'

    def test_console_outputs_number_of_mentions_written(self, capfd):

        second_altmetric = Altmetric()
        second_altmetric.altmetric_id = 9876
        second_altmetric.doi = '/Second/Test/DOI/5678'

        second_mention = Mention()
        second_mention.url = 'http://testurl2.com'

        second_altmetric.add_mention(second_mention)

        self.test_csv_writer_facade.write(second_altmetric)

        out, err = capfd.readouterr()
        assert out == '1 mentions successfully written for altmetric with DOI /Second/Test/DOI/5678\n'
