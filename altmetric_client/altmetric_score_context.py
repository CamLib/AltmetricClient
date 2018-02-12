class AltmetricScoreContext:

    def __init__(self):

        self.__context_type = None
        self.__total_no_of_other_articles = None
        self.__mean = None
        self.__rank = None
        self.__this_scored_higher_than_pct = None
        self.__this_scored_higher_than = None
        self.__rank_type = None
        self.__percentile = None

    @property
    def context_type(self):
        return self.__context_type

    @context_type.setter
    def context_type(self, context_type):
        self.__context_type = context_type

    @property
    def total_number_of_other_articles(self):
        return self.__total_no_of_other_articles

    @total_number_of_other_articles.setter
    def total_number_of_other_articles(self, total_no_of_other_articles):
        self.__total_no_of_other_articles = total_no_of_other_articles

    @property
    def mean(self):
        return self.__mean

    @mean.setter
    def mean(self, mean):
        self.__mean = mean

    @property
    def rank(self):
        return self.__rank

    @rank.setter
    def rank(self, rank):
        self.__rank = rank

    @property
    def this_scored_higher_than_pct(self):
        return self.__this_scored_higher_than_pct

    @this_scored_higher_than_pct.setter
    def this_scored_higher_than_pct(self, this_scored_higher_than_pct):
        self.__this_scored_higher_than_pct = this_scored_higher_than_pct

    @property
    def this_scored_higher_than(self):
        return self.__this_scored_higher_than

    @this_scored_higher_than.setter
    def this_scored_higher_than(self, this_scored_higher_than):
        self.this_scored_higher_than = this_scored_higher_than

    @property
    def rank_type(self):
        return self.__rank_type

    @rank_type.setter
    def rank_type(self, rank_type):
        self.__rank_type = rank_type

    @property
    def percentile(self):
        return self.__percentile

    @percentile.setter
    def percentile(self, percentile):
        self.__percentile = percentile
