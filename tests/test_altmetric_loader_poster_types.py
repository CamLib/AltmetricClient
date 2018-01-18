from altmetric_client.altmetric_loader import AltmetricLoader
from altmetric_client.author_manager import AuthorManager

import json

class TestAltmetricLoaderPosterTypes:

    def setup_method(self):

        extraFieldsJsonFile = open("json_data/101Mentions.json")

        test_data = json.load(extraFieldsJsonFile)

        test_author_manager = AuthorManager()
        test_altmetric_loader = AltmetricLoader()
        test_altmetric_loader.author_manager = test_author_manager

        self.result = test_altmetric_loader.parse_result(test_data)

        extraFieldsJsonFile.close()

    def test_poster_type_members_of_public_count_added(self):

        assert int(self.result.poster_type_members_of_public_count) == 55

    def test_poster_type_researcher_count_added(self):

        assert int(self.result.poster_type_researcher_count) == 6

    def test_poster_type_practitioner(self):

        assert int(self.result.poster_type_practitioner_count) == 9

    def test_poster_type_science_communicator(self):

        assert int(self.result.poster_type_science_communicator_count) == 0
