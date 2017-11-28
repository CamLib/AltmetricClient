import json

from altmetric_client.altmetric_loader import AltmetricLoader
from altmetric_client.author_manager import AuthorManager

class TestAuthorLoading:

    '''Need to test this with an altmetric that has F1000 as a source of mentions
    (as they are ones that definitely don't have authors)'''

    def setup_method(self):

        test_author_manager = AuthorManager()
        test_altmetric_loader = AltmetricLoader()

        test_altmetric_loader.author_manager = test_author_manager

        mentionsJsonFile = open("json_data/10Mentions.json")

        test_data = json.load(mentionsJsonFile)

        test_altmetric_loader.parse_result(test_data)

        self.test_authors_list = test_altmetric_loader.authors_list

    def test_ten_authors_loaded(self):

        assert len(self.test_authors_list) == 8

