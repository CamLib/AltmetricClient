from csv import DictWriter
from altmetric_client.altmetric_score import AltmetricScore

from altmetric_client.output_writer_csv.csv_writer_base import CSVWriterBase

class CSVWriterScores(CSVWriterBase):

    def __init__(self,
                 output_file_name=None,
                 output_directory_name=None,
                 altmetric_scores=None):

        CSVWriterBase.__init__(self, output_file_name, output_directory_name)
        self.__altmetric_scores = altmetric_scores

    @property
    def altmetric_scores(self):
        return self.__altmetric_scores

    @altmetric_scores.setter
    def altmetric_scores(self, altmetric_scores: AltmetricScore):
        self.altmetric_scores = altmetric_scores

    def write_scores(self):

        output_file_path = '{0}{1}'.format(self.output_directory_name, self.output_file_name)

        write_mode = self._get_write_mode(output_file_path)

        fieldnames = ['doi', 'total', 'history_1y', 'history_6m', 'history_3m', 'history_1m', 'history_1w',
                      'history_6d', 'history_5d', 'history_4d', 'history_3d', 'history_2d', 'history_1d',
                      'context_all_total_articles', 'context_all_mean', 'context_all_rank',
                      'context_all_scored_higher_than_pct', 'context_all_scored_higher_than',
                      'context_all_rank_type', 'context_all_percentile',
                      'context_similar_age_3m_total_articles', 'context_similar_age_3m_mean', 'context_similar_age_3m_rank',
                      'context_similar_age_3m_scored_higher_than_pct', 'context_similar_age_3m_scored_higher_than',
                      'context_similar_age_3m_rank_type', 'context_similar_age_3m_percentile',
                      'context_this_journal_total_articles', 'context_this_journal_mean',
                      'context_this_journal_rank',
                      'context_this_journal_scored_higher_than_pct', 'context_this_journal_scored_higher_than',
                      'context_this_journal_rank_type', 'context_this_journal_percentile',
                      'context_similar_age_this_journal_3m_total_articles', 'context_similar_age_this_journal_3m_mean',
                      'context_similar_age_this_journal_3m_rank',
                      'context_similar_age_this_journal_3m_scored_higher_than_pct', 'context_similar_age_this_journal_3m_scored_higher_than',
                      'context_similar_age_this_journal_3m_rank_type', 'context_similar_age_this_journal_3m_percentile',
                      ]

        try:

            with open(output_file_path, write_mode) as output_csv:

                output_writer = DictWriter(output_csv, fieldnames=fieldnames)

                if write_mode == 'w':

                    output_writer.writeheader()

                output_dict = dict(doi=self.__altmetric_scores.doi,
                                    total=self.__altmetric_scores.total_score,
                                    history_1y=self.__altmetric_scores.score_history.last_one_year,
                                    history_6m=self.__altmetric_scores.score_history.last_six_months,
                                    history_3m=self.__altmetric_scores.score_history.last_three_months,
                                    history_1m=self.__altmetric_scores.score_history.last_one_month,
                                    history_1w=self.__altmetric_scores.score_history.last_one_week,
                                    history_6d=self.__altmetric_scores.score_history.last_six_days,
                                    history_5d=self.__altmetric_scores.score_history.last_five_days,
                                    history_4d=self.__altmetric_scores.score_history.last_four_days,
                                    history_3d=self.__altmetric_scores.score_history.last_three_days,
                                    history_2d=self.__altmetric_scores.score_history.last_two_days,
                                    history_1d=self.__altmetric_scores.score_history.last_one_day,
                                    context_all_total_articles=self.__altmetric_scores.context_all.total_number_of_other_articles,
                                    context_all_mean=self.__altmetric_scores.context_all.mean,
                                    context_all_rank=self.__altmetric_scores.context_all.rank,
                                    context_all_scored_higher_than_pct=self.__altmetric_scores.context_all.this_scored_higher_than_pct,
                                    context_all_scored_higher_than=self.__altmetric_scores.context_all.this_scored_higher_than,
                                    context_all_rank_type=self.__altmetric_scores.context_all.rank_type,
                                    context_all_percentile=self.__altmetric_scores.context_all.percentile,
                                    context_similar_age_3m_total_articles=self.__altmetric_scores.context_similar_age_three_months.total_number_of_other_articles,
                                    context_similar_age_3m_mean=self.__altmetric_scores.context_similar_age_three_months.mean,
                                    context_similar_age_3m_rank=self.__altmetric_scores.context_similar_age_three_months.rank,
                                    context_similar_age_3m_scored_higher_than_pct=self.__altmetric_scores.context_similar_age_three_months.this_scored_higher_than_pct,
                                    context_similar_age_3m_scored_higher_than=self.__altmetric_scores.context_similar_age_three_months.this_scored_higher_than,
                                    context_similar_age_3m_rank_type=self.__altmetric_scores.context_similar_age_three_months.rank_type,
                                    context_similar_age_3m_percentile=self.__altmetric_scores.context_similar_age_three_months.percentile,
                                    context_this_journal_total_articles=self.__altmetric_scores.context_this_journal.total_number_of_other_articles,
                                    context_this_journal_mean=self.__altmetric_scores.context_this_journal.mean,
                                    context_this_journal_rank=self.__altmetric_scores.context_this_journal.rank,
                                    context_this_journal_scored_higher_than_pct=self.__altmetric_scores.context_this_journal.this_scored_higher_than_pct,
                                    context_this_journal_scored_higher_than=self.__altmetric_scores.context_this_journal.this_scored_higher_than,
                                    context_this_journal_rank_type=self.__altmetric_scores.context_this_journal.rank_type,
                                    context_this_journal_percentile=self.__altmetric_scores.context_this_journal.percentile,
                                    context_similar_age_this_journal_3m_total_articles=self.__altmetric_scores.context_similar_age_this_journal_three_months.total_number_of_other_articles,
                                    context_similar_age_this_journal_3m_mean=self.__altmetric_scores.context_similar_age_this_journal_three_months.mean,
                                    context_similar_age_this_journal_3m_rank=self.__altmetric_scores.context_similar_age_this_journal_three_months.rank,
                                    context_similar_age_this_journal_3m_scored_higher_than_pct=self.__altmetric_scores.context_similar_age_this_journal_three_months.this_scored_higher_than_pct,
                                    context_similar_age_this_journal_3m_scored_higher_than=self.__altmetric_scores.context_similar_age_this_journal_three_months.this_scored_higher_than,
                                    context_similar_age_this_journal_3m_rank_type=self.__altmetric_scores.context_similar_age_this_journal_three_months.rank_type,
                                    context_similar_age_this_journal_3m_percentile=self.__altmetric_scores.context_similar_age_this_journal_three_months.percentile,
                                   )

                output_writer.writerow(output_dict)

        except:

            print('Something totally unexpected happened when trying to write to a Scores CSV file')
            print('The writer was setup to write to a file called {0}{1}'.format(self.output_directory_name,
                                                                                 self.output_file_name))
            if write_mode == 'a':
                print('The writer thought this file existed and was trying to append to it.')
            elif write_mode == 'w':

                print('The writer thought this was a brand new file and was trying to create it.')
            else:
                print('The writer could not determine whether or not the file existed.')