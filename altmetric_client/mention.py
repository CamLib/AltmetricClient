class Mention:

    def __init__(self):

        self.__related_article_doi = None
        self.__source = None
        self.__url = None
        self.__date_posted = None

    @property
    def related_article_doi(self):

        return self.__related_article_doi

    @related_article_doi.setter
    def related_article_doi(self, related_article_doi):
        self.__related_article_doi = related_article_doi

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, source):
        self.__source = source

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url):
        self.__url = url

    @property
    def date_posted(self):
        return self.__date_posted

    @date_posted.setter
    def date_posted(self, date_posted):
        self.__date_posted = date_posted