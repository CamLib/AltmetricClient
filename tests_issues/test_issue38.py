from altmetric_client.altmetric_loader import AltmetricLoader
from altmetric_client.author_manager import AuthorManager

import json

class TestIssue38:

    def _load_result(self, path_to_json):

        test_json_data = open(path_to_json)

        test_data = json.load(test_json_data)

        test_author_manager = AuthorManager()
        test_altmetric_loader = AltmetricLoader()
        test_altmetric_loader.author_manager = test_author_manager

        result = test_altmetric_loader.parse_result(test_data)

        test_json_data.close()

        return result


    def test_journal_title_for_01_is_NA(self):

        result = self._load_result("json_data/38_01.json")

        assert result.journal_title == 'NA'

    def test_title_for_02(self):

        result = self._load_result("json_data/38_02.json")

        assert result.article_title == 'International Social Survey Programme: Social Inequality IV - ISSP 2009'

    def test_publisher_for_03(self):

        result = self._load_result("json_data/38_03.json")

        assert result.publisher == 'Oxfam'

    def test_first_author_for_04(self):

        result = self._load_result("json_data/38_04.json")

        assert result.first_author == 'NA'

    def test_type_for_05(self):

        result = self._load_result("json_data/38_05.json")

        assert result.type == 'chapter'

    def test_type_for_06(self):

        result = self._load_result("json_data/38_06.json")

        assert result.type == 'article'

    def test_type_for_07(self):

        result = self._load_result("json_data/38_07.json")

        assert result.type == 'article'

    def test_type_for_08(self):

        result = self._load_result("json_data/38_08.json")

        assert result.type == 'article'

    def test_type_for_09(self):

        result = self._load_result("json_data/38_09.json")

        assert result.type == 'article'

    def test_type_for_10(self):

        result = self._load_result("json_data/38_10.json")

        assert result.type == 'article'

    def test_type_for_11(self):

        result = self._load_result("json_data/38_11.json")

        assert result.type == 'article'

    def test_type_for_12(self):

        result = self._load_result("json_data/38_12.json")

        assert result.type == 'article'

    def test_type_for_13(self):

        result = self._load_result("json_data/38_13.json")

        assert result.type == 'article'




