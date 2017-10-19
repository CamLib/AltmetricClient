class Altmetric:

    def __init__(self):

        self.__altmetric_id = None
        self.__altmetric_score = None
        self.__article_title = None
        self.__journal_title = None
        self.__altmetric_journal_id = None
        self.__total_mentions = None
        self.__print_publication_date = None
        self.__first_seen_on_date = None
        self.__first_author = None

    @property
    def altmetric_id(self):
        return self.__altmetric_id

    @altmetric_id.setter
    def altmetric_id(self, altmetric_id):
        self.__altmetric_id = altmetric_id

    @property
    def altmetric_score(self):
        return self.__altmetric_score

    @altmetric_score.setter
    def altmetric_score(self, altmetric_score):
        self.__altmetric_score = altmetric_score

    @property
    def article_title(self):
        return self.__article_title

    @article_title.setter
    def article_title(self, article_title):
        self.__article_title = article_title

    @property
    def journal_title(self):
        return self.__journal_title

    @journal_title.setter
    def journal_title(self, journal_title):
        self.__journal_title = journal_title

    @property
    def altmetric_journal_id(self):
        return self.__altmetric_journal_id

    @altmetric_journal_id.setter
    def altmetric_journal_id(self, altmetric_journal_id):
        self.__altmetric_journal_id = altmetric_journal_id

    @property
    def total_mentions(self):
        return self.__total_mentions

    @total_mentions.setter
    def total_mentions(self, total_mentions):
        self.__total_mentions = total_mentions

    @property
    def print_publication_date(self):
        return self.__print_publication_date

    @print_publication_date.setter
    def print_publication_date(self, print_publication_date):
        self.__print_publication_date = print_publication_date

    @property
    def first_seen_on_date(self):
        return self.__first_seen_on_date

    @first_seen_on_date.setter
    def first_seen_on_date(self, first_seen_on_date):
        self.__first_seen_on_date = first_seen_on_date

    @property
    def first_author(self):
        return self.__first_author

    @first_author.setter
    def first_author(self, authors):
        self.__first_author = authors

