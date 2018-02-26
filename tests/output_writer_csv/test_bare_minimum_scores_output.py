import os

from altmetric_client.altmetric_score import AltmetricScore
from altmetric_client.altmetric_score_context import AltmetricScoreContext
from altmetric_client.altmetric_score_history import AltmetricScoreHistory

from altmetric_client.output_writer_csv.csv_writer_scores import CSVWriterScores

from csv import DictReader

class TestBareMinimumScores:

    def setup_method(self):

        self._files_out_directory = '../files_out/'
        self._test_file_name = 'test_bare_minimum_scores_file.csv'

        # clean up the old test file in the setup

        filepath = '{0}{1}'.format(self._files_out_directory, self._test_file_name)

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
        test_context_all_time.total_number_of_other_articles = 1000
        test_context_all_time.mean = 5
        test_context_all_time.rank = 500
        test_context_all_time.this_scored_higher_than_pct = 50
        test_context_all_time.this_scored_higher_than = 499
        test_context_all_time.rank_type = "test rank type 1"
        test_context_all_time.percentile = 51

        test_scores.context_all = test_context_all_time

        test_context_similar_age_three_months = AltmetricScoreContext()
        test_context_similar_age_three_months.total_number_of_other_articles = 200
        test_context_similar_age_three_months.mean = 4
        test_context_similar_age_three_months.rank = 150
        test_context_similar_age_three_months.this_scored_higher_than_pct = 74
        test_context_similar_age_three_months.this_scored_higher_than = 149
        test_context_similar_age_three_months.rank_type = "test rank type 2"
        test_context_similar_age_three_months.percentile = 75

        test_scores.context_similar_age_three_months = test_context_similar_age_three_months

        test_context_this_journal = AltmetricScoreContext()
        test_context_this_journal.total_number_of_other_articles = 100
        test_context_this_journal.mean = 3
        test_context_this_journal.rank = 80
        test_context_this_journal.this_scored_higher_than_pct = 79
        test_context_this_journal.this_scored_higher_than = 78
        test_context_this_journal.rank_type = "test rank type 3"
        test_context_this_journal.percentile = 81

        test_scores.context_this_journal = test_context_this_journal

        test_context_similar_age_this_journal_three_months = AltmetricScoreContext()
        test_context_similar_age_this_journal_three_months.total_number_of_other_articles = 50
        test_context_similar_age_this_journal_three_months.mean = 2
        test_context_similar_age_this_journal_three_months.rank = 45
        test_context_similar_age_this_journal_three_months.this_scored_higher_than_pct = 90
        test_context_similar_age_this_journal_three_months.this_scored_higher_than = 44
        test_context_similar_age_this_journal_three_months.rank_type = "test rank type 4"
        test_context_similar_age_this_journal_three_months.percentile = 89

        test_scores.context_similar_age_this_journal_three_months = test_context_similar_age_this_journal_three_months

        self.test_csv_writer_scores = CSVWriterScores(self._test_file_name,
                                                        self._files_out_directory,
                                                        test_scores)

    def tear_down_method(self):
        self.test_csv_writer_scores = None

    def test_file_name_added(self):

        assert self.test_csv_writer_scores.output_file_name == 'test_bare_minimum_scores_file.csv'

    def test_output_directory_added(self):

        assert self.test_csv_writer_scores.output_directory_name == '../files_out/'

    def test_scores_added(self):

        assert self.test_csv_writer_scores.altmetric_scores.doi == 'test/DOI/1'

    def test_file_created_with_header_containing_geo_demographic_source(self):

        self.test_csv_writer_scores.write_scores()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:

            test_output_reader = DictReader(test_output_csv)
            assert test_output_reader.fieldnames[2] == 'history_1y'

    def test_doi_added_to_scores(self):

        self.test_csv_writer_scores.write_scores()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['doi'] == "test/DOI/1"

    def test_total_added_to_scores(self):

        self.test_csv_writer_scores.write_scores()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['total'] == "16384"

    def test_history_1y_added_to_scores(self):

        self.test_csv_writer_scores.write_scores()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['history_1y'] == "8192"

    def test_history_6m_added_to_scores(self):

        self.test_csv_writer_scores.write_scores()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['history_6m'] == "4095"

    def test_history_3m_added_to_scores(self):

        self.test_csv_writer_scores.write_scores()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['history_3m'] == "2048"

    def test_history_1m_added_to_scores(self):

        self.test_csv_writer_scores.write_scores()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['history_1m'] == "1024"

    def test_history_1w_added_to_scores(self):

        self.test_csv_writer_scores.write_scores()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['history_1w'] == "512"

    def test_history_6d_added_to_scores(self):

        self.test_csv_writer_scores.write_scores()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['history_6d'] == "256"

    def test_history_5d_added_to_scores(self):

        self.test_csv_writer_scores.write_scores()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['history_5d'] == "128"

    def test_history_4d_added_to_scores(self):

        self.test_csv_writer_scores.write_scores()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['history_4d'] == "64"

    def test_history_3d_added_to_scores(self):

        self.test_csv_writer_scores.write_scores()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['history_3d'] == "32"

    def test_history_2d_added_to_scores(self):

        self.test_csv_writer_scores.write_scores()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['history_2d'] == "16"

    def test_history_1d_added_to_scores(self):

        self.test_csv_writer_scores.write_scores()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['history_1d'] == "8"

    def test_context_all_total_articles_added_to_scores(self):

        self.test_csv_writer_scores.write_scores()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['context_all_total_articles'] == "1000"

    def test_context_all_mean_added_to_scores(self):

        self.test_csv_writer_scores.write_scores()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['context_all_mean'] == "5"

    def test_context_all_rank_added_to_scores(self):

        self.test_csv_writer_scores.write_scores()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['context_all_rank'] == "500"

    def test_context_all_scored_higher_than_pct_added_to_scores(self):

        self.test_csv_writer_scores.write_scores()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['context_all_scored_higher_than_pct'] == "50"

    def test_context_all_scored_higher_than_added_to_scores(self):

        self.test_csv_writer_scores.write_scores()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['context_all_scored_higher_than'] == "499"

    def test_context_all_rank_type_added_to_scores(self):

        self.test_csv_writer_scores.write_scores()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['context_all_rank_type'] == "test rank type 1"

    def test_context_all_percentile_added_to_scores(self):

        self.test_csv_writer_scores.write_scores()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['context_all_percentile'] == "51"

    def test_context_3m_total_articles_added_to_scores(self):

        self.test_csv_writer_scores.write_scores()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['context_similar_age_3m_total_articles'] == "200"

    def test_context_3m_mean_added_to_scores(self):

        self.test_csv_writer_scores.write_scores()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['context_similar_age_3m_mean'] == "4"

    def test_context_3m_rank_added_to_scores(self):

        self.test_csv_writer_scores.write_scores()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['context_similar_age_3m_rank'] == "150"

    def test_context_3m_scored_higher_than_pct_added_to_scores(self):

        self.test_csv_writer_scores.write_scores()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['context_similar_age_3m_scored_higher_than_pct'] == "74"

    def test_context_3m_scored_higher_than_added_to_scores(self):

        self.test_csv_writer_scores.write_scores()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['context_similar_age_3m_scored_higher_than'] == "149"

    def test_context_3m_rank_type_added_to_scores(self):

        self.test_csv_writer_scores.write_scores()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['context_similar_age_3m_rank_type'] == "test rank type 2"

    def test_context_3m_percentile_added_to_scores(self):

        self.test_csv_writer_scores.write_scores()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['context_similar_age_3m_percentile'] == "75"

    def test_context_journal_total_articles_added_to_scores(self):

        self.test_csv_writer_scores.write_scores()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['context_this_journal_total_articles'] == "100"

    def test_context_journal_mean_added_to_scores(self):

        self.test_csv_writer_scores.write_scores()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['context_this_journal_mean'] == "3"

    def test_context_journal_rank_added_to_scores(self):

        self.test_csv_writer_scores.write_scores()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['context_this_journal_rank'] == "80"

    def test_context_journal_scored_higher_than_pct_added_to_scores(self):

        self.test_csv_writer_scores.write_scores()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['context_this_journal_scored_higher_than_pct'] == "79"

    def test_context_journal_scored_higher_than_added_to_scores(self):

        self.test_csv_writer_scores.write_scores()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['context_this_journal_scored_higher_than'] == "78"

    def test_context_journal_rank_type_added_to_scores(self):

        self.test_csv_writer_scores.write_scores()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['context_this_journal_rank_type'] == "test rank type 3"

    def test_context_journal_percentile_added_to_scores(self):

        self.test_csv_writer_scores.write_scores()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['context_this_journal_percentile'] == "81"

    def test_context_3m_journal_total_articles_added_to_scores(self):

        self.test_csv_writer_scores.write_scores()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['context_similar_age_this_journal_3m_total_articles'] == "50"

    def test_context_3m_journal_mean_added_to_scores(self):

        self.test_csv_writer_scores.write_scores()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['context_similar_age_this_journal_3m_mean'] == "2"

    def test_context_3m_journal_rank_added_to_scores(self):

        self.test_csv_writer_scores.write_scores()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['context_similar_age_this_journal_3m_rank'] == "45"

    def test_context_3m_journal_scored_higher_than_pct_added_to_scores(self):

        self.test_csv_writer_scores.write_scores()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['context_similar_age_this_journal_3m_scored_higher_than_pct'] == "90"

    def test_context_3m_journal_scored_higher_than_added_to_scores(self):

        self.test_csv_writer_scores.write_scores()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['context_similar_age_this_journal_3m_scored_higher_than'] == "44"

    def test_context_3m_journal_rank_type_added_to_scores(self):

        self.test_csv_writer_scores.write_scores()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['context_similar_age_this_journal_3m_rank_type'] == "test rank type 4"

    def test_context_3m_journal_percentile_added_to_scores(self):

        self.test_csv_writer_scores.write_scores()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:
            test_output_reader = DictReader(test_output_csv)

            assert next(test_output_reader)['context_similar_age_this_journal_3m_percentile'] == "89"

