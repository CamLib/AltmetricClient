import os
from csv import DictReader
from altmetric_client.output_writer_csv.csv_writer_geo_demographics import CSVWriterGeoDemographics
from altmetric_client.geo_demographics import GeoDemographics

class TestBareMinimumGeoDemographics:

    def setup_method(self):

        self._files_out_directory = '../files_out/'
        self._test_file_name = 'test_bare_minimum_geo_demographics_file.csv'

        # clean up the old test file in the setup

        filepath = '{0}{1}'.format(self._files_out_directory, self._test_file_name)

        if os.path.isfile(filepath):
            os.remove(filepath)

        test_geo_demographics_list = []

        test_geo_demographics1 = GeoDemographics()
        test_geo_demographics1.doi = "Test/Geo/DOI_1"
        test_geo_demographics1.source = "TestSource1"
        test_geo_demographics1.country_code = "TEST1"
        test_geo_demographics1.total = 1234

        test_geo_demographics_list.append(test_geo_demographics1)

        test_geo_demographics2 = GeoDemographics()
        test_geo_demographics2.doi = "Test/Geo/DOI_2"
        test_geo_demographics2.source = "TestSource2"
        test_geo_demographics2.country_code = "TEST2"
        test_geo_demographics2.total = 4321

        test_geo_demographics_list.append(test_geo_demographics2)

        self.test_csv_writer_geo_demographics = CSVWriterGeoDemographics(self._test_file_name,
                                                                           self._files_out_directory,
                                                                           test_geo_demographics_list)


    def tear_down_method(self):
        self.test_csv_writer_geo_demographics = None

    def test_file_name_added(self):

        assert self.test_csv_writer_geo_demographics.output_file_name == 'test_bare_minimum_geo_demographics_file.csv'

    def test_output_directory_added(self):

        assert self.test_csv_writer_geo_demographics.output_directory_name == '../files_out/'

    def test_geo_demographics_list_added(self):

        assert self.test_csv_writer_geo_demographics.geo_demographics_list[0].doi == 'Test/Geo/DOI_1'

    def test_file_created_with_header_containing_geo_demographic_source(self):

        self.test_csv_writer_geo_demographics.write_geo_demographics()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:

            test_output_reader = DictReader(test_output_csv)
            assert test_output_reader.fieldnames[1] == 'geo_demographic_source'

    def test_doi_added_to_geo_demographics(self):

        self.test_csv_writer_geo_demographics.write_geo_demographics()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['doi'] == "Test/Geo/DOI_1"

    def test_geo_demographic_source_added_to_geo_demographics(self):

        self.test_csv_writer_geo_demographics.write_geo_demographics()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['geo_demographic_source'] == "TestSource1"

    def test_country_code_added_to_geo_demographics(self):

        self.test_csv_writer_geo_demographics.write_geo_demographics()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['country_code'] == "TEST1"

    def test_geo_demographic_total_added_to_geo_demographics(self):

        self.test_csv_writer_geo_demographics.write_geo_demographics()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['geo_demographic_total'] == "1234"

    def test_second_line_added(self):

        self.test_csv_writer_geo_demographics.write_geo_demographics()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            next(test_output_reader)

            assert next(test_output_reader)['geo_demographic_total'] == "4321"
