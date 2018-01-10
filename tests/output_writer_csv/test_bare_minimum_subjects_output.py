import os
from csv import DictReader
from altmetric_client.output_writer_csv.csv_writer_subject import CSVWriterSubject
from altmetric_client.subject import Subject

class TestBareMinimumSubjectsOutput:

    def setup_method(self):

        self._files_out_directory = '../files_out/'
        self._test_file_name = 'test_bare_minimum_subjects_file.csv'

        # clean up the old test file in the setup

        filepath = '{0}{1}'.format(self._files_out_directory, self._test_file_name)

        if os.path.isfile(filepath):
            os.remove(filepath)

        test_subjects_list = []

        test_subject_1 = Subject()
        test_subject_1.doi = "Subject/test/doi_1"
        test_subject_1.scheme = "TestScheme1"
        test_subject_1.name = "TestName1"

        test_subjects_list.append(test_subject_1)

        test_subject_2 = Subject()
        test_subject_2.doi = "Subject/test/doi_2"
        test_subject_2.scheme = "TestScheme2"
        test_subject_2.name = "TestName2"

        test_subjects_list.append(test_subject_2)

        self.test_csv_writer_subjects = CSVWriterSubject(self._test_file_name,
                                                         self._files_out_directory,
                                                         test_subjects_list)

    def tear_down_method(self):

        self.test_csv_writer_subjects = None

    def test_file_name_added(self):

        assert self.test_csv_writer_subjects.output_file_name == 'test_bare_minimum_subjects_file.csv'

    def test_output_directory_added(self):

        assert self.test_csv_writer_subjects.output_directory_name == '../files_out/'

    def test_subjects_list_added(self):

        assert self.test_csv_writer_subjects.subjects_list[0].doi == 'Subject/test/doi_1'

    def test_file_created_with_header_containing_doi(self):

        self.test_csv_writer_subjects.write_subjects()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:

            test_output_reader = DictReader(test_output_csv)
            assert test_output_reader.fieldnames[0] == 'doi'

    def test_doi_added_to_subjects(self):

        self.test_csv_writer_subjects.write_subjects()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['doi'] == 'Subject/test/doi_1'

    def test_scheme_added_to_subjects(self):

        self.test_csv_writer_subjects.write_subjects()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['subject_scheme'] == 'TestScheme1'

    def test_name_added_to_subjects(self):

        self.test_csv_writer_subjects.write_subjects()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['subject_name'] == 'TestName1'

    def test_second_subject_added(self):

        self.test_csv_writer_subjects.write_subjects()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            next(test_output_reader)

            assert next(test_output_reader)['subject_name'] == 'TestName2'

    def test_extra_subjects_appended_to_existing_file(self):

        self.test_csv_writer_subjects.write_subjects()

        extra_subjects = []

        third_subject = Subject()
        third_subject.doi = 'Subject/Test/doi_3'
        third_subject.scheme = 'TestScheme3'
        third_subject.name = 'TestName3'

        extra_subjects.append(third_subject)

        self.test_csv_writer_subjects.subjects_list = extra_subjects

        self.test_csv_writer_subjects.write_subjects()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:

            test_output_reader = DictReader(test_output_csv)

            next(test_output_reader)
            next(test_output_reader)

            assert next(test_output_reader)['doi'] == 'Subject/Test/doi_3'