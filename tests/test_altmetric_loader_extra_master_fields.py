from altmetric_client.altmetric_loader import AltmetricLoader
from altmetric_client.author_manager import AuthorManager

import json

class TestAlmetricLoaderExtraMasterFields:

    def setup_method(self):

        extraFieldsJsonFile = open("json_data/10Mentions.json")

        test_data = json.load(extraFieldsJsonFile)

        test_author_manager = AuthorManager()
        test_altmetric_loader = AltmetricLoader()
        test_altmetric_loader.author_manager = test_author_manager

        self.result = test_altmetric_loader.parse_result(test_data)

        extraFieldsJsonFile.close()

    def test_page_start_added(self):

        assert self.result.page_starts == "23"

    def test_end_page_added(self):

        assert self.result.page_ends == "33"

    def test_journal_issue_added(self):

        assert self.result.journal_issue == "1"

    def test_last_mention_date_added(self):

        assert self.result.last_mentioned_date == "2014-10-15T11:00"

