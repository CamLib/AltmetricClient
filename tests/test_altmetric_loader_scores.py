from altmetric_client.altmetric_loader import AltmetricLoader
from altmetric_client.author_manager import AuthorManager

import json

class TestAltmetricLoaderScores:

    def setup_method(self):

        mentionsJsonFile = open("json_data/10Mentions.json")

        test_data = json.load(mentionsJsonFile)

        test_author_manager = AuthorManager()
        test_altmetric_loader = AltmetricLoader()
        test_altmetric_loader.author_manager = test_author_manager

        self.result = test_altmetric_loader.parse_result(test_data)

        mentionsJsonFile.close()

    def test_score_total_is_38_etc(self):

        assert self.result.scores.total_score == 38.358

    def test_one_year_history_score(self):

        assert self.result.scores.score_history.last_one_year == 11

    def test_six_month_history_score(self):

        assert self.result.scores.score_history.last_six_months == 10

    def test_three_month_history_score(self):

        assert self.result.scores.score_history.last_three_months == 9

    def test_one_month_history_score(self):

        assert self.result.scores.score_history.last_one_month == 8

    def test_one_week_history_score(self):

        assert self.result.scores.score_history.last_one_week == 7

    def test_six_day_history_score(self):

        assert self.result.scores.score_history.last_six_days == 6

    def test_five_day_history_score(self):

        assert self.result.scores.score_history.last_five_days == 5

    def test_four_day_history_score(self):

        assert self.result.scores.score_history.last_four_days == 4

    def test_three_day_history_score(self):

        assert self.result.scores.score_history.last_three_days == 3

    def test_two_day_history_score(self):

        assert self.result.scores.score_history.last_two_days == 2

    def test_one_day_history_score(self):

        assert self.result.scores.score_history.last_one_day == 1

    def test_all_context_total_other_articles(self):

        assert self.result.scores.context_all.total_number_of_other_articles == 8048343

    def test_all_context_mean(self):

        assert self.result.scores.context_all.mean == 6.8380049254832

    def test_all_context_rank(self):

        assert self.result.scores.context_all.rank == 223745

    def test_all_context_this_scored_higher_than_pct(self):

        assert self.result.scores.context_all.this_scored_higher_than_pct == 97

    def test_all_context_this_scored_higher_than(self):

        assert self.result.scores.context_all.this_scored_higher_than == 7825458

    def test_all_context_rank_type(self):

        assert self.result.scores.context_all.rank_type == "exact"

    def test_all_context_percentile(self):

        assert self.result.scores.context_all.percentile == 97

    def test_similar_age_context_total_other_articles(self):

        assert self.result.scores.context_similar_age_three_months.total_number_of_other_articles == 250200

    def test_this_journal_context_total_other_articles(self):

        assert self.result.scores.context_this_journal.total_number_of_other_articles == 601

    def test_similar_age_this_journal_context_total_other_articles(self):

        assert self.result.scores.context_similar_age_this_journal_three_months.total_number_of_other_articles == 23