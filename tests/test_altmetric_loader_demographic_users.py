from altmetric_client.altmetric_loader import AltmetricLoader
from altmetric_client.author_manager import AuthorManager

import json

class TestAltmetricLoaderDemographicUsers:

    def setup_method(self):

        mentionsJsonFile = open("json_data/101Mentions.json")

        test_data = json.load(mentionsJsonFile)

        test_author_manager = AuthorManager()
        test_altmetric_loader = AltmetricLoader()
        test_altmetric_loader.author_manager = test_author_manager

        self.result = test_altmetric_loader.parse_result(test_data)

        mentionsJsonFile.close()

    def test_three_twitter_cohorts_returned(self):

        twitter_cohorts = [user_demographics for user_demographics in self.result.user_demographics
                           if user_demographics.source == 'twitter' and user_demographics.group_type == 'cohort']

        assert len(twitter_cohorts) == 3

    def test_researcher_cohort_scientists_is_six(self):

        scientists_twitter_cohort = [user_demographics for user_demographics in self.result.user_demographics
                           if user_demographics.source == 'twitter' and user_demographics.group_type == 'cohort'
                                     and user_demographics.group_value == 'Scientists']

        assert scientists_twitter_cohort[0].total == 6

    def test_nine_mendeley_by_status_demographics_returned(self):

        mendeley_by_status = [user_demographics for user_demographics in self.result.user_demographics
                           if user_demographics.source == 'mendeley' and user_demographics.group_type == 'by_status']

        assert len(mendeley_by_status) == 9

    def test_other_status_demographic_total_is_three(self):

        other_mendeley_status_demographics = [user_demographics for user_demographics in self.result.user_demographics
                           if user_demographics.source == 'mendeley' and user_demographics.group_type == 'by_status'
                                              and user_demographics.group_value == 'Other']

        assert other_mendeley_status_demographics[0].total == 3

    def test_nine_mendeley_by_discipline_demographics_returned(self):

        mendeley_by_discipline = [user_demographics for user_demographics in self.result.user_demographics
                           if user_demographics.source == 'mendeley' and user_demographics.group_type == 'by_discipline']

        assert len(mendeley_by_discipline) == 9

    def test_psychology_by_discipline_demographic_total_is_thirteen(self):

        mendeley_psychology_discipline = [user_demographics for user_demographics in self.result.user_demographics
                                            if user_demographics.source == 'mendeley' and
                                          user_demographics.group_type == 'by_discipline' and
                                          user_demographics.group_value == 'Psychology']

        assert mendeley_psychology_discipline[0].total == 13

    def test_altmetric_poster_type_demographic_member_of_public_is_55(self):

        altmetric_poster_type_public = [user_demographics for user_demographics in self.result.user_demographics
                                        if user_demographics.source == 'altmetric'
                                        and user_demographics.group_type == 'poster_types'
                                        and user_demographics.group_value == 'member_of_the_public']

        assert altmetric_poster_type_public[0].total == 55
