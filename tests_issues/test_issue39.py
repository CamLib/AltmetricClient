from altmetric_client.altmetric_loader import AltmetricLoader
from altmetric_client.author_manager import AuthorManager

import json

class TestIssue39:

    def _load_result(self, path_to_json):

        test_json_data = open(path_to_json)

        test_data = json.load(test_json_data)

        test_author_manager = AuthorManager()
        test_altmetric_loader = AltmetricLoader()
        test_altmetric_loader.author_manager = test_author_manager

        result = test_altmetric_loader.parse_result(test_data)

        test_json_data.close()

        return result


    def test_pubdate_for_01_is_NA(self):

        result = self._load_result("json_data/39_01.json")

        assert result.print_publication_date == 'NA'

    def test_type_for_02_is_article(self):

        result = self._load_result("json_data/39_02.json")

        assert result.type == 'article'

    def test_type_for_03_is_article(self):

        result = self._load_result("json_data/39_03.json")

        assert result.type == 'article'

    def test_type_for_04_is_article(self):

        result = self._load_result("json_data/39_04.json")

        assert result.type == 'article'

    def test_type_for_05_is_article(self):

        result = self._load_result("json_data/39_05.json")

        assert result.type == 'article'

    def test_type_for_06_is_article(self):

        result = self._load_result("json_data/39_06.json")

        assert result.type == 'article'

    def test_type_for_07_is_article(self):

        result = self._load_result("json_data/39_07.json")

        assert result.type == 'article'

    def test_title_for_08(self):

        result = self._load_result("json_data/39_08.json")

        assert result.article_title == 'Revolutionizing Arts Education in K-12 Classrooms through Technological Integration'

    def test_type_for_09_is_article(self):

        result = self._load_result("json_data/39_09.json")

        assert result.type == 'article'

    def test_type_for_10_is_article(self):

        result = self._load_result("json_data/39_10.json")

        assert result.type == 'article'

    def test_type_for_11_is_article(self):

        result = self._load_result("json_data/39_11.json")

        assert result.type == 'article'

    def test_type_for_12_is_article(self):

        result = self._load_result("json_data/39_12.json")

        assert result.type == 'article'

    def test_type_for_13_is_article(self):

        result = self._load_result("json_data/39_13.json")

        assert result.type == 'article'

    def test_type_for_14_is_article(self):

        result = self._load_result("json_data/39_14.json")

        assert result.type == 'article'

    def test_type_for_15_is_article(self):

        result = self._load_result("json_data/39_15.json")

        assert result.type == 'article'

    def test_type_for_16_is_article(self):

        result = self._load_result("json_data/39_16.json")

        assert result.type == 'article'

    def test_first_seen_on_date_for_17_is_NA(self):

        result = self._load_result("json_data/39_17.json")

        assert result.first_seen_on_date == 'NA'

    def test_type_for_18_is_article(self):

        result = self._load_result("json_data/39_18.json")

        assert result.type == 'article'

    def test_type_for_19_is_article(self):

        result = self._load_result("json_data/39_19.json")

        assert result.type == 'article'

    def test_type_for_20_is_article(self):

        result = self._load_result("json_data/39_20.json")

        assert result.type == 'article'

    def test_type_for_21_is_article(self):

        result = self._load_result("json_data/39_21.json")

        assert result.type == 'article'

    def test_type_for_22_is_article(self):

        result = self._load_result("json_data/39_22.json")

        assert result.type == 'article'

    def test_type_for_23_is_article(self):

        result = self._load_result("json_data/39_23.json")

        assert result.type == 'article'

    def test_type_for_24_is_article(self):

        result = self._load_result("json_data/39_24.json")

        assert result.type == 'article'

    def test_type_for_25_is_article(self):

        result = self._load_result("json_data/39_25.json")

        assert result.type == 'article'

    def test_type_for_26_is_article(self):

        result = self._load_result("json_data/39_26.json")

        assert result.type == 'article'

    def test_type_for_27_is_article(self):

        result = self._load_result("json_data/39_27.json")

        assert result.type == 'article'

    def test_type_for_28_is_article(self):

        result = self._load_result("json_data/39_28.json")

        assert result.type == 'article'

    def test_type_for_29_is_article(self):

        result = self._load_result("json_data/39_29.json")

        assert result.type == 'article'

    def test_type_for_30_is_article(self):

        result = self._load_result("json_data/39_30.json")

        assert result.type == 'article'

    def test_type_for_31_is_article(self):

        result = self._load_result("json_data/39_31.json")

        assert result.type == 'article'

    def test_type_for_32_is_article(self):

        result = self._load_result("json_data/39_32.json")

        assert result.type == 'article'

    def test_type_for_33_is_article(self):

        result = self._load_result("json_data/39_33.json")

        assert result.type == 'article'

    def test_type_for_34_is_article(self):

        result = self._load_result("json_data/39_34.json")

        assert result.type == 'article'

    def test_type_for_35_is_article(self):

        result = self._load_result("json_data/39_35.json")

        assert result.type == 'article'

    def test_type_for_36_is_article(self):

        result = self._load_result("json_data/39_36.json")

        assert result.type == 'article'

    def test_type_for_37_is_article(self):

        result = self._load_result("json_data/39_37.json")

        assert result.type == 'article'