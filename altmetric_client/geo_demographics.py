class GeoDemograhics:

    def __init__(self):

        self.__doi = None
        self.__source = None
        self.__country_code = None
        self.__total = None

    @property
    def doi(self):
        return self.__doi

    @doi.setter
    def doi(self, doi):
        self.__doi = doi

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, source):
        self.__source = source

    @property
    def country_code(self):
        return self.__country_code

    @country_code.setter
    def country_code(self, country_code):
        self.__country_code = country_code

    @property
    def total(self):
        return self.__total

    @total.setter
    def total(self, total):
        self.__total = total