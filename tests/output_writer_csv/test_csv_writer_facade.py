import os
from csv import DictReader

from altmetric_client.output_writer_csv.csv_writer_facade import CSVWriterFacade
from altmetric_client.altmetric import Altmetric
from altmetric_client.mention import Mention
from altmetric_client.author import Author
from altmetric_client.subject import Subject
from altmetric_client.user_demographics import UserDemographics
from altmetric_client.geo_demographics import GeoDemographics

class TestCSVWriterFacade:

    def setup_method(self):

        test_file_root = 'test_csv_facade'
        output_directory_name = '../files_out/'

        self.master_filepath = '{0}{1}_master.csv'.format(output_directory_name, test_file_root)
        self.mentions_filepath = '{0}{1}_mentions.csv'.format(output_directory_name, test_file_root)
        self.authors_filepath = '{0}{1}_authors.csv'.format(output_directory_name, test_file_root)
        self.subjects_filepath = '{0}{1}_subjects.csv'.format(output_directory_name, test_file_root)
        self.user_demographics_filepath = '{0}{1}_user_demographics.csv'.format(output_directory_name, test_file_root)
        self.geo_demographics_filepath = '{0}{1}_geo_demographics.csv'.format(output_directory_name, test_file_root)

        # clean up the old test files in the setup

        if os.path.isfile(self.master_filepath):
            os.remove(self.master_filepath)

        if os.path.isfile(self.mentions_filepath):
            os.remove(self.mentions_filepath)

        if os.path.isfile(self.authors_filepath):
            os.remove(self.authors_filepath)

        if os.path.isfile(self.subjects_filepath):
            os.remove(self.subjects_filepath)

        if os.path.isfile(self.user_demographics_filepath):
            os.remove(self.user_demographics_filepath)

        if os.path.isfile(self.geo_demographics_filepath):
            os.remove(self.geo_demographics_filepath)

        test_altmetric = Altmetric()
        test_altmetric.altmetric_id = 1234
        test_altmetric.doi = "/Test/DOI/1234"

        test_mention = Mention()
        test_mention.related_article_doi = "/Test/DOI/1234"
        test_mention.url = "http://testurl1.com"
        test_altmetric.add_mention(test_mention)

        test_subject = Subject()
        test_subject.name = 'TestSubject'
        test_altmetric.add_subject(test_subject)

        test_user_demographics = UserDemographics()
        test_user_demographics.group_value = 'Test Demographic Group Value'
        test_altmetric.add_user_demographics(test_user_demographics)

        test_geo_demographics = GeoDemographics()
        test_geo_demographics.country_code = 'TEST1'
        test_altmetric.add_geo_demographics(test_geo_demographics)

        test_authors_list = []
        test_author = Author()
        test_author.author_id = 'testsource1'
        test_authors_list.append(test_author)

        self.test_csv_writer_facade = CSVWriterFacade(output_directory_name, test_file_root)
        self.test_csv_writer_facade.write(test_altmetric)
        self.test_csv_writer_facade.write_authors(test_authors_list)

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

    def test_mention_from_second_altmetric_written_to_mentions(self):

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

    def test_console_outputs_numbers_of_data_written(self, capfd):

        second_altmetric = Altmetric()
        second_altmetric.altmetric_id = 9876
        second_altmetric.doi = '/Second/Test/DOI/5678'

        second_mention = Mention()
        second_mention.url = 'http://testurl2.com'

        second_altmetric.add_mention(second_mention)

        second_subject = Subject()
        second_subject.name = 'TestSubject2'

        second_altmetric.add_subject(second_subject)

        second_user_demographic = UserDemographics()
        second_user_demographic.source = 'Test source'

        second_altmetric.add_user_demographics(second_user_demographic)

        second_geo_demographic = GeoDemographics()
        second_geo_demographic.source = 'Test source'

        second_altmetric.add_geo_demographics(second_geo_demographic)

        self.test_csv_writer_facade.write(second_altmetric)

        out, err = capfd.readouterr()
        assert out == '1 mentions successfully written for altmetric with DOI /Second/Test/DOI/5678\n' \
                      '1 subjects successfully written for altmetric with DOI /Second/Test/DOI/5678\n' \
                      '1 user demographics successfully written for altmetric with DOI /Second/Test/DOI/5678\n' \
                      '1 geo demographics successfully written for altmetric with DOI /Second/Test/DOI/5678\n'

    def test_subject_written(self):

        with open(self.subjects_filepath) as test_subjects_output_csv:

            test_output_reader = DictReader(test_subjects_output_csv)
            assert next(test_output_reader)['subject_name'] == 'TestSubject'

    def test_user_demographics_written(self):

        with open(self.user_demographics_filepath) as test_user_demographics_output_csv:

            test_output_reader = DictReader(test_user_demographics_output_csv)
            assert next(test_output_reader)['demographic_group_value'] == 'Test Demographic Group Value'

    def test_geo_demographics_written(self):

        with open(self.geo_demographics_filepath) as test_geo_demographics_output_csv:

            test_output_reader = DictReader(test_geo_demographics_output_csv)
            assert next(test_output_reader)['country_code'] == 'TEST1'

    def test_authors_written(self):

        with open(self.authors_filepath) as test_authors_output_csv:

            test_output_reader = DictReader(test_authors_output_csv)
            assert next(test_output_reader)['author_id'] == 'testsource1'

    def test_console_outputs_number_of_authors_written(self, capfd):

        second_authors_list = []
        second_author = Author()
        second_author.author_id = 'testsource2'
        second_authors_list.append(second_author)

        self.test_csv_writer_facade.write_authors(second_authors_list)

        out, err = capfd.readouterr()
        assert out == '1 authors successfully written\n'
