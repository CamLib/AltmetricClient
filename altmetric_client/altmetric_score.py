from altmetric_client.altmetric_score_context import AltmetricScoreContext

class AltmetricScore:

    def __init__(self):

        self.__doi = None
        self.__total_score = None
        self.__score_history = None
        self.__score_context = []

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
    def score_history(self, score_history):
        self.__score_history = score_history

    @property
    def score_context(self):
        return self.__score_context

    def add_score_context(self, score_context:AltmetricScoreContext):
        self.__score_context.append(score_context)