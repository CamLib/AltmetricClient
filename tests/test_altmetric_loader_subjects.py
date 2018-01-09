from altmetric_client.altmetric_loader import AltmetricLoader
from altmetric_client.altmetric import Altmetric
from altmetric_client.author_manager import AuthorManager
from altmetric_client.subject import Subject

import json

class TestAltmetricLoaderSubjects:

    def setup_method(self):

        mentionsJsonFile = open("json_data/10Mentions.json")

        test_data = json.load(mentionsJsonFile)

        test_author_manager = AuthorManager()
        test_altmetric_loader = AltmetricLoader()
        test_altmetric_loader.author_manager = test_author_manager

        self.result = test_altmetric_loader.parse_result(test_data)

        mentionsJsonFile.close()

    def test_one_altmetric_subject_loaded(self):

        altmetric_subjects = [subject for subject in self.result.subjects if subject.scheme == 'altmetric']

        assert len(altmetric_subjects) == 1

    def test_altmetric_subject_loaded_with_name_environmentalhealth(self):

        altmetric_subjects = [subject for subject in self.result.subjects if subject.scheme == 'altmetric']

        assert altmetric_subjects[0].name == 'environmentalhealth'

    def test_three_scopus_subjects_loaded(self):

        scopus_subjects = [subject for subject in self.result.subjects if subject.scheme == 'scopus']

        assert len(scopus_subjects) == 3

    def test_last_scopus_subject_is_physical_sciences(self):

        scopus_subjects = [subject for subject in self.result.subjects if subject.scheme == 'scopus']

        assert scopus_subjects[2].name == 'Physical Sciences'

    def test_one_era_subject_loaded(self):

        era_subjects = [subject for subject in self.result.subjects if subject.scheme == 'era']

        assert len(era_subjects) == 1

    def test_era_subject_is_multidisciplinary(self):

        era_subjects = [subject for subject in self.result.subjects if subject.scheme == 'era']

        assert era_subjects[0].name == 'Multidisciplinary'

    def test_five_subjects_loaded_overall(self):

        assert len(self.result.subjects) == 5