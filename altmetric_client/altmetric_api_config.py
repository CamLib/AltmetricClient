class AltmetricAPIConfig:

    def __init__(self):

        self.__api_base_uri = None
        self.__api_version = None
        self.__api_base_command = None
        self.__api_requested_item_id_type = None
        self.__api_key = None


    @property
    def api_base_uri(self):
        return self.__api_base_uri

    @api_base_uri.setter
    def api_base_uri(self, api_base_uri):
        self.__api_base_uri = api_base_uri

    @property
    def api_version(self):
        return self.__api_version

    @api_version.setter
    def api_version(self, api_version):
        self.__api_version = api_version

    @property
    def api_base_command(self):
        return self.__api_base_command

    @api_base_command.setter
    def api_base_command(self, api_base_command):
        self.__api_base_command = api_base_command

    @property
    def api_requested_item_id_type(self):
        return self.__api_requested_item_id_type

    @api_requested_item_id_type.setter
    def api_requested_item_id_type(self, api_requested_item_id_type):
        self.__api_requested_item_id_type = api_requested_item_id_type

    @property
    def api_key(self):
        return self.__api_key

    @api_key.setter
    def api_key(self, api_key):
        self.__api_key = api_key
