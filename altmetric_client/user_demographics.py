class UserDemographics:

    def __init__(self):

        self.__doi = None
        self.__source = None
        self.__group_type = None
        self.__group_value = None
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
    def group_type(self):
        return self.__group_type

    @group_type.setter
    def group_type(self, group_type):
        self.__group_type = group_type

    @property
    def group_value(self):
        return self.__group_value

    @group_value.setter
    def group_value(self, group_value):
        self.__group_value = group_value

    @property
    def total(self):
        return self.__total

    @total.setter
    def total(self, total):
        self.__total = total
