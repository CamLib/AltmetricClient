class Subject:

    def __init__(self):

        self.__doi = None
        self.__scheme = None
        self.__name = None

    @property
    def doi(self):
        return self.__doi

    @doi.setter
    def doi(self, doi):
        self.__doi = doi

    @property
    def scheme(self):
        return self.__scheme

    @scheme.setter
    def scheme(self, scheme):
        self.__scheme = scheme

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
