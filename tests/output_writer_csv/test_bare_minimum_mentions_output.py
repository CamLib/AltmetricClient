import os
from csv import DictReader
from altmetric_client.output_writer_csv.csv_writer_mentions import CSVWriterMention
from altmetric_client.mention import Mention

class TestBareMinimumMentionsOutput:

    def setup_method(self):

        self._test_file_name = 'test_bare_minimum_mentions_file.csv'
        self._files_out_directory = '../files_out/'

        # clean up the old test file in the setup

        filepath = '{0}{1}'.format(self._files_out_directory, self._test_file_name)

        if os.path.isfile(filepath):
            os.remove(filepath)

        test_mentions_list = []

        test_mention_1 = Mention()
        test_mention_1.related_article_doi = '/Test/DOI/1234'
        test_mention_1.url = 'http://testurl1.com'
        test_mention_1.source = 'testsource1'
        test_mention_1.date_posted = '2016-03-31T11:00:00+00:00'
        test_mention_1.author_id = 'testsource11'

        test_mentions_list.append(test_mention_1)

        test_mention_2 = Mention()
        test_mention_2.related_article_doi = '/Test/DOI/4321'
        test_mention_2.url = 'http://testurl2.com'
        test_mention_2.source = 'testsource22'
        test_mention_2.date_posted = '2015-03-15T12:00:00+00:00'
        test_mention_2.author_id = 'testsource21'

        test_mentions_list.append(test_mention_2)

        self.test_csv_writer_mentions = CSVWriterMention(self._test_file_name,
                                                         self._files_out_directory,
                                                         test_mentions_list)

    def tear_down_method(self):

        self.test_csv_writer_mentions = None

    def test_file_name_added(self):

        assert self.test_csv_writer_mentions.output_file_name == 'test_bare_minimum_mentions_file.csv'

    def test_output_directory_added(self):

        assert self.test_csv_writer_mentions.output_directory_name == '../files_out/'

    def test_mentions_list_added(self):

        assert self.test_csv_writer_mentions.mentions_list[0].url == 'http://testurl1.com'

    def test_file_created_with_header_containing_related_article_doi(self):

        self.test_csv_writer_mentions.write_mentions()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:

            test_output_reader = DictReader(test_output_csv)
            assert test_output_reader.fieldnames[0] == 'related_article_doi'

    def test_related_article_doi_added_to_mentions(self):

        self.test_csv_writer_mentions.write_mentions()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['related_article_doi'] == '/Test/DOI/1234'

    def test_url_added_to_mentions(self):

        self.test_csv_writer_mentions.write_mentions()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['url'] == 'http://testurl1.com'

    def test_source_added_to_mentions(self):

        self.test_csv_writer_mentions.write_mentions()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['source'] == 'testsource1'

    def test_date_posted_added_to_mentions(self):

        self.test_csv_writer_mentions.write_mentions()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['date_posted'] == '2016-03-31T11:00:00+00:00'

    def test_author_id_added_to_mentions(self):

        self.test_csv_writer_mentions.write_mentions()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['author_id'] == 'testsource11'

    def test_second_mention_url_added(self):

        self.test_csv_writer_mentions.write_mentions()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            next(test_output_reader)

            assert next(test_output_reader)['url'] == 'http://testurl2.com'

    def test_extra_mentions_appended_to_existing_file(self):

        self.test_csv_writer_mentions.write_mentions()

        extra_mentions = []
        third_mention = Mention()
        third_mention.related_article_doi = '/Test/DOI/3/9876'
        third_mention.url = 'http://testurl3.com'
        third_mention.source = 'testsource3'
        third_mention.date_posted = '2014-03-15T13:00:00+00:00'
        third_mention.date_posted = 'testsource33'

        extra_mentions.append(third_mention)

        self.test_csv_writer_mentions.mentions_list = extra_mentions

        self.test_csv_writer_mentions.write_mentions()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:

            test_output_reader = DictReader(test_output_csv)

            next(test_output_reader)
            next(test_output_reader)

            assert next(test_output_reader)['url'] == 'http://testurl3.com'