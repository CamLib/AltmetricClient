from altmetric_client.altmetric_loader import AltmetricLoader
from altmetric_client.author_manager import AuthorManager

import json

class TestAltmetricLoaderDemographicGeo:

    def setup_method(self):

        mentionsJsonFile = open("json_data/10Mentions.json")

        test_data = json.load(mentionsJsonFile)

        test_author_manager = AuthorManager()
        test_altmetric_loader = AltmetricLoader()
        test_altmetric_loader.author_manager = test_author_manager

        self.result = test_altmetric_loader.parse_result(test_data)

        mentionsJsonFile.close()

    def test_twitter_geo_has_one_demographic(self):

        twitter_geo_demographics = [geo_demographics for geo_demographics in self.result.geo_demographics
                           if geo_demographics.source == 'twitter']

        assert len(twitter_geo_demographics) == 1

    def test_twitter_geo_country_code_is_GB(self):

        twitter_geo_demographics = [geo_demographics for geo_demographics in self.result.geo_demographics
                                    if geo_demographics.source == 'twitter']

        assert twitter_geo_demographics[0].country_code == 'GB'

    def test_twitter_geo_total_is_1(self):

        twitter_geo_demographics = [geo_demographics for geo_demographics in self.result.geo_demographics
                                    if geo_demographics.source == 'twitter']

        assert twitter_geo_demographics[0].total == 1

    def test_mendeley_geo_has_six(self):

        mendeley_geo_demographics = [geo_demographics for geo_demographics in self.result.geo_demographics
                           if geo_demographics.source == 'mendeley']

        assert len(mendeley_geo_demographics) == 6

