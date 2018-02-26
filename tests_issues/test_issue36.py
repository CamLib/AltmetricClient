from altmetric_client.altmetric_loader import AltmetricLoader
from altmetric_client.author_manager import AuthorManager
from altmetric_client.altmetric_score import AltmetricScore
from altmetric_client.altmetric_score_history import AltmetricScoreHistory
from altmetric_client.altmetric_score_context import AltmetricScoreContext
from altmetric_client.output_writer_csv.csv_writer_scores import CSVWriterScores
from csv import DictReader

import json
import os

class TestIssue36:

    def _load_result(self, path_to_json):

        test_json_data = open(path_to_json)

        test_data = json.load(test_json_data)

        test_author_manager = AuthorManager()
        test_altmetric_loader = AltmetricLoader()
        test_altmetric_loader.author_manager = test_author_manager

        result = test_altmetric_loader.parse_result(test_data)

        test_json_data.close()

        return result

    def test_context_all_total_articles_for_file_1_is_na(self):

        result = self._load_result("json_data/36_01.json")

        assert result.scores.context_all.total_number_of_other_articles == 'na'

    def test_context_all_mean_for_file_2_is_na(self):

        result = self._load_result("json_data/36_02.json")

        assert result.scores.context_all.mean == 'na'

    def test_context_all_percentile_for_file_3_is_na(self):

        result = self._load_result("json_data/36_03.json")

        assert result.scores.context_all.percentile == 'na'

    def test_context_all_rank_for_file_1_is_na(self):

        result = self._load_result("json_data/36_01.json")

        assert result.scores.context_all.rank == 'na'

    def test_context_all_this_scored_higher_than_pct_for_file_1_is_na(self):

        result = self._load_result("json_data/36_01.json")

        assert result.scores.context_all.this_scored_higher_than_pct == 'na'

    def test_context_all_this_scored_higher_than_for_file_1_is_na(self):

        result = self._load_result("json_data/36_01.json")

        assert result.scores.context_all.this_scored_higher_than == 'na'

    def test_context_all_rank_type_for_file_1_is_na(self):

        result = self._load_result("json_data/36_01.json")

        assert result.scores.context_all.rank_type == 'na'

    def test_demographics_load_without_poster_types(self):

        result = self._load_result("json_data/36_01.json")

        assert len(result.user_demographics) == 25


    def test_scores_writer_copes_with_nas_in_contexts(self):

        files_out_directory = '../files_out/'
        test_file_name = 'test_issue_36.csv'

        # clean up the old test file

        filepath = '{0}{1}'.format(files_out_directory, test_file_name)

        if os.path.isfile(filepath):
            os.remove(filepath)

        test_scores = AltmetricScore()

        test_scores.doi = "test/DOI/1"
        test_scores.total_score = 16384

        test_score_history = AltmetricScoreHistory()
        test_score_history.last_one_year = 8192
        test_score_history.last_six_months = 4095
        test_score_history.last_three_months = 2048
        test_score_history.last_one_month = 1024
        test_score_history.last_one_week = 512
        test_score_history.last_six_days = 256
        test_score_history.last_five_days = 128
        test_score_history.last_four_days = 64
        test_score_history.last_three_days = 32
        test_score_history.last_two_days = 16
        test_score_history.last_one_day = 8

        test_scores.score_history = test_score_history

        test_context_all_time = AltmetricScoreContext()
        test_context_all_time.total_number_of_other_articles = 'na'
        test_context_all_time.mean = 'na'
        test_context_all_time.rank = 'na'
        test_context_all_time.this_scored_higher_than_pct = 'na'
        test_context_all_time.this_scored_higher_than = 'na'
        test_context_all_time.rank_type = "na"
        test_context_all_time.percentile = 'na'

        test_scores.context_all = test_context_all_time

        test_context_similar_age_three_months = AltmetricScoreContext()
        test_context_similar_age_three_months.total_number_of_other_articles = 'na'
        test_context_similar_age_three_months.mean = 'na'
        test_context_similar_age_three_months.rank = 'na'
        test_context_similar_age_three_months.this_scored_higher_than_pct = 'na'
        test_context_similar_age_three_months.this_scored_higher_than = 'na'
        test_context_similar_age_three_months.rank_type = 'na'
        test_context_similar_age_three_months.percentile = 'na'

        test_scores.context_similar_age_three_months = test_context_similar_age_three_months

        test_context_this_journal = AltmetricScoreContext()
        test_context_this_journal.total_number_of_other_articles = 'na'
        test_context_this_journal.mean = 'na'
        test_context_this_journal.rank = 'na'
        test_context_this_journal.this_scored_higher_than_pct = 'na'
        test_context_this_journal.this_scored_higher_than = 'na'
        test_context_this_journal.rank_type = 'na'
        test_context_this_journal.percentile = 'na'

        test_scores.context_this_journal = test_context_this_journal

        test_context_similar_age_this_journal_three_months = AltmetricScoreContext()
        test_context_similar_age_this_journal_three_months.total_number_of_other_articles = 'na'
        test_context_similar_age_this_journal_three_months.mean = 'na'
        test_context_similar_age_this_journal_three_months.rank = 'na'
        test_context_similar_age_this_journal_three_months.this_scored_higher_than_pct = 'na'
        test_context_similar_age_this_journal_three_months.this_scored_higher_than = 'na'
        test_context_similar_age_this_journal_three_months.rank_type = 'na'
        test_context_similar_age_this_journal_three_months.percentile = 'na'

        test_scores.context_similar_age_this_journal_three_months = test_context_similar_age_this_journal_three_months

        self.test_csv_writer_scores = CSVWriterScores(test_file_name,
                                                        files_out_directory,
                                                        test_scores)

        self.test_csv_writer_scores.write_scores()

        with open('{0}{1}'.format(files_out_directory, test_file_name)) as test_output_csv:

            test_output_reader = DictReader(test_output_csv)
            assert next(test_output_reader)['context_all_scored_higher_than_pct'] == "na"
