

class Altmetric:

    def __init__(self):

        self.__journal_title = None
        self.__altmetric_score = None


    @property
    def journal_title(self):
        return self.__journal_title

    @journal_title.setter
    def journal_title(self, journal_title):
        self.__journal_title = journal_title

    @property
    def altmetric_score(self):
        return self.__altmetric_score

    @altmetric_score.setter
    def altmetric_score(self, altmetric_score):
        self.__altmetric_score = altmetric_score