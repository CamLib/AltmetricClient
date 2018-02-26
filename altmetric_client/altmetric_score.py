from altmetric_client.altmetric_score_context import AltmetricScoreContext
from altmetric_client.altmetric_score_history import AltmetricScoreHistory

class AltmetricScore:

    def __init__(self):

        self.__doi = None
        self.__total_score = None
        self.__score_history = None
        self.__context_all = None
        self.__context_similar_age_three_months = None
        self.__context_this_journal = None
        self.__context_similar_age_this_journal_three_months = None

    @property
    def doi(self):
        return self.__doi

    @doi.setter
    def doi(self, doi):
        self.__doi = doi

    @property
    def total_score(self):
        return self.__total_score

    @total_score.setter
    def total_score(self, total_score):
        self.__total_score = total_score

    @property
    def score_history(self):
        return self.__score_history

    @score_history.setter
    def score_history(self, score_history: AltmetricScoreHistory):
        self.__score_history = score_history

    @property
    def context_all(self):
        return self.__context_all

    @context_all.setter
    def context_all(self, context_all: AltmetricScoreContext):
        self.__context_all = context_all

    @property
    def context_similar_age_three_months(self):
        return self.__context_similar_age_three_months

    @context_similar_age_three_months.setter
    def context_similar_age_three_months(self, similar_age_three_months: AltmetricScoreContext):
        self.__context_similar_age_three_months = similar_age_three_months

    @property
    def context_this_journal(self):
        return self.__context_this_journal

    @context_this_journal.setter
    def context_this_journal(self, context_this_journal: AltmetricScoreContext):
        self.__context_this_journal = context_this_journal

    @property
    def context_similar_age_this_journal_three_months(self):
        return self.__context_similar_age_this_journal_three_months

    @context_similar_age_this_journal_three_months.setter
    def context_similar_age_this_journal_three_months(self, context_similar_age_this_journal_three_months: AltmetricScoreContext):
        self.__context_similar_age_this_journal_three_months = context_similar_age_this_journal_three_months
