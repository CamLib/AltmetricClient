class Author:

    def __init__(self):

        self.__author_id = None
        self.__source = None
        self.__name = None
        self.__url = None
        self.__image_url = None
        self.__description = None
        self.__id_on_source = None
        self.__followers = None

    @property
    def author_id(self):
        return self.__author_id

    @author_id.setter
    def author_id(self, author_id: str):
        self.__author_id = author_id

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, source):
        self.__source = source

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def image_url(self):
        return self.__image_url

    @image_url.setter
    def image(self, image_url: str):
        self.__image_url = image_url

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def id_on_source(self):
        return self.__id_on_source

    @id_on_source.setter
    def id_on_source(self, id_on_source: str):
        self.__id_on_source = id_on_source

    @property
    def followers(self):
        return self.__followers

    @followers.setter
    def followers(self, followers: int):
        self.__followers = followers