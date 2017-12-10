from altmetric_client.author import Author
from altmetric_client.output_writer_csv.csv_writer_author import CSVWriterAuthor
from csv import DictReader
import os

class TestBareMinimumAuthorOutput:

    def setup_method(self):

        self._test_file_name = 'test_bare_minimum_authors_file.csv'
        self._files_out_directory = '../files_out/'

        # clean up the old test file in the setup

        filepath = '{0}{1}'.format(self._files_out_directory, self._test_file_name)

        if os.path.isfile(filepath):
            os.remove(filepath)

        test_authors_list = []

        test_author_1 = Author()
        test_author_1.author_id = 'testsource1'
        test_author_1.name = 'Test Name 1'
        test_author_1.source = 'testsource'
        test_author_1.url = 'http://testurl1.com'
        test_author_1.id_on_source = 'test_id_on_source1'
        test_author_1.description = 'Test Author 1 Description'
        test_author_1.image_url = 'http://testurl1.com/image1.jpg'
        test_author_1.followers = 1

        test_authors_list.append(test_author_1)

        test_author_2 = Author()
        test_author_2.author_id = 'testsource2'
        test_author_2.name = 'Test Name 2'
        test_author_2.source = 'testsource'
        test_author_2.url = 'http://testurl2.com'
        test_author_2.id_on_source = 'test_id_on_source2'
        test_author_2.description = 'Test Author 2 Description'
        test_author_2.image_url = 'http://testurl2.com/image1.jpg'
        test_author_2.followers = 2

        test_authors_list.append(test_author_2)

        self.test_csv_writer_authors = CSVWriterAuthor(self._test_file_name, self._files_out_directory, test_authors_list)

    def tear_down_method(self):

        self.test_csv_writer_authors = None

    def test_file_name_added(self):

        self.test_csv_writer_authors.output_file_name = 'Test Output File Name'
        assert 'Test Output File Name' == self.test_csv_writer_authors.output_file_name

    def test_directory_name_added(self):

        self.test_csv_writer_authors.output_directory_name = 'Test Output Dir Name'
        assert 'Test Output Dir Name' == self.test_csv_writer_authors.output_directory_name

    def test_authors_list_added(self):

        assert len(self.test_csv_writer_authors.authors_list) == 2

    def test_file_created_with_header_containing_doi(self):

        self.test_csv_writer_authors.write_authors()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:

            test_output_reader = DictReader(test_output_csv)
            assert test_output_reader.fieldnames[0] == 'author_id'

    def test_author_id_added_to_csv(self):

        self.test_csv_writer_authors.write_authors()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['author_id'] == 'testsource1'

    def test_author_name_added_to_csv(self):

        self.test_csv_writer_authors.write_authors()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['author_name'] == 'Test Name 1'

    def test_author_source_added_to_csv(self):

        self.test_csv_writer_authors.write_authors()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['author_source'] == 'testsource'

    def test_author_url_added_to_csv(self):

        self.test_csv_writer_authors.write_authors()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['author_url'] == 'http://testurl1.com'

    def test_author_id_on_source_added_to_csv(self):

        self.test_csv_writer_authors.write_authors()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['author_id_on_source'] == 'test_id_on_source1'

    def test_author_description(self):

        self.test_csv_writer_authors.write_authors()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['author_description'] == 'Test Author 1 Description'

    def test_author_image_url(self):

        self.test_csv_writer_authors.write_authors()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['author_image_url'] == 'http://testurl1.com/image1.jpg'

    def test_author_followers(self):

        self.test_csv_writer_authors.write_authors()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert int(next(test_output_reader)['author_follower_count']) == 1

    def test_second_author_added(self):

        self.test_csv_writer_authors.write_authors()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)
            next(test_output_reader)
            assert int(next(test_output_reader)['author_follower_count']) == 2
