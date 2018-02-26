class AltmetricScoreHistory:

    def __init__(self):

        self.__last_one_year = None
        self.__last_six_months = None
        self.__last_three_months = None
        self.__last_one_month = None
        self.__last_one_week = None
        self.__last_six_days = None
        self.__last_five_days = None
        self.__last_four_days = None
        self.__last_three_days = None
        self.__last_two_days = None
        self.__last_one_day = None

    @property
    def last_one_year(self):
        return self.__last_one_year

    @last_one_year.setter
    def last_one_year(self, last_one_year):
        self.__last_one_year = last_one_year

    @property
    def last_six_months(self):
        return self.__last_six_months

    @last_six_months.setter
    def last_six_months(self, last_six_months):
        self.__last_six_months = last_six_months

    @property
    def last_three_months(self):
        return self.__last_three_months

    @last_three_months.setter
    def last_three_months(self, last_three_months):
        self.__last_three_months = last_three_months

    @property
    def last_one_month(self):
        return self.__last_one_month

    @last_one_month.setter
    def last_one_month(self, last_one_month):
        self.__last_one_month = last_one_month

    @property
    def last_one_week(self):
        return self.__last_one_week

    @last_one_week.setter
    def last_one_week(self, last_one_week):
        self.__last_one_week = last_one_week

    @property
    def last_six_days(self):
        return self.__last_six_days

    @last_six_days.setter
    def last_six_days(self, last_six_days):
        self.__last_six_days = last_six_days

    @property
    def last_five_days(self):
        return self.__last_five_days

    @last_five_days.setter
    def last_five_days(self, last_five_days):
        self.__last_five_days = last_five_days

    @property
    def last_four_days(self):
        return self.__last_four_days

    @last_four_days.setter
    def last_four_days(self, last_four_days):
        self.__last_four_days = last_four_days

    @property
    def last_three_days(self):
        return self.__last_three_days

    @last_three_days.setter
    def last_three_days(self, last_three_days):
        self.__last_three_days = last_three_days

    @property
    def last_two_days(self):
        return self.__last_two_days

    @last_two_days.setter
    def last_two_days(self, last_two_days):
        self.__last_two_days = last_two_days

    @property
    def last_one_day(self):
        return self.__last_one_day

    @last_one_day.setter
    def last_one_day(self, last_one_day):
        self.__last_one_day = last_one_day