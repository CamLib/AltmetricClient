import os
from csv import DictReader
from altmetric_client.output_writer_csv.csv_writer_user_demographics import CSVWriterUserDemographics
from altmetric_client.user_demographics import UserDemographics


class TestBareMinimumUserDemographics:

    def setup_method(self):

        self._files_out_directory = '../files_out/'
        self._test_file_name = 'test_bare_minimum_user_demographics_file.csv'

        # clean up the old test file in the setup

        filepath = '{0}{1}'.format(self._files_out_directory, self._test_file_name)

        if os.path.isfile(filepath):
            os.remove(filepath)

        test_user_demographics_list = []

        test_user_demographics1 = UserDemographics()
        test_user_demographics1.doi = "/Test/doi/0001"
        test_user_demographics1.group_type = "Test Demographic Group Type 1"
        test_user_demographics1.group_value = "Test Demographic Group Value 1"
        test_user_demographics1.source = "Test Demographic Source 1"
        test_user_demographics1.total = 101

        test_user_demographics_list.append(test_user_demographics1)

        test_user_demographics2 = UserDemographics()
        test_user_demographics2.doi = "/Test/doi/0002"
        test_user_demographics2.group_type = "Test Demographic Group Type 2"
        test_user_demographics2.group_value = "Test Demographic Group Value 2"
        test_user_demographics2.source = "Test Demographic Source 2"
        test_user_demographics2.total = 102

        test_user_demographics_list.append(test_user_demographics2)

        self.test_csv_writer_user_demographics = CSVWriterUserDemographics(self._test_file_name,
                                                                             self._files_out_directory,
                                                                             test_user_demographics_list)

    def tear_down_method(self):
        self.test_csv_writer_user_demographics = None

    def test_file_name_added(self):

        assert self.test_csv_writer_user_demographics.output_file_name == 'test_bare_minimum_user_demographics_file.csv'

    def test_output_directory_added(self):

        assert self.test_csv_writer_user_demographics.output_directory_name == '../files_out/'

    def test_user_demographics_list_added(self):

        assert self.test_csv_writer_user_demographics.user_demographics_list[0].doi == '/Test/doi/0001'

    def test_file_created_with_header_containing_demographic_group_type(self):

        self.test_csv_writer_user_demographics.write_user_demographics()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:

            test_output_reader = DictReader(test_output_csv)
            assert test_output_reader.fieldnames[2] == 'demographic_group_type'

    def test_doi_added_to_user_demographics(self):

        self.test_csv_writer_user_demographics.write_user_demographics()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['doi'] == "/Test/doi/0001"

    def test_demographic_source_added_to_user_demographics(self):

        self.test_csv_writer_user_demographics.write_user_demographics()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['demographic_source'] == "Test Demographic Source 1"

    def test_demographic_group_type_added_to_user_demographics(self):

        self.test_csv_writer_user_demographics.write_user_demographics()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['demographic_group_type'] == "Test Demographic Group Type 1"

    def test_demographic_group_value_added_to_user_demographics(self):

        self.test_csv_writer_user_demographics.write_user_demographics()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['demographic_group_value'] == "Test Demographic Group Value 1"

    def test_demographic_total_added_to_user_demographics(self):

        self.test_csv_writer_user_demographics.write_user_demographics()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['demographic_total'] == "101"

    def test_second_line_added(self):

        self.test_csv_writer_user_demographics.write_user_demographics()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            next(test_output_reader)

            assert next(test_output_reader)['demographic_total'] == "102"
