from altmetric_client.altmetric_api_config import AltmetricAPIConfig

class URLBuilder:

    def __init__(self, altmetric_api_config: AltmetricAPIConfig = None, doi: str = None):

        self._altmetric_api_config = altmetric_api_config
        self._doi = doi

    @property
    def altmetric_api_config(self):

        return self._altmetric_api_config

    @altmetric_api_config.setter
    def altmetric_api_config(self, altmetric_api_config : AltmetricAPIConfig):

        self._altmetric_api_config = altmetric_api_config

    @property
    def doi(self):

        return self._doi

    @doi.setter
    def doi(self, doi):

        self._doi = doi

    def build_url(self):

        url = ''

        if self._altmetric_api_config.api_base_uri:
            url = self._altmetric_api_config.api_base_uri

        if self._altmetric_api_config.api_version:
            url = url + '/{0}'.format(self._altmetric_api_config.api_version)

        if self._altmetric_api_config.api_base_command:
            url = url + '/{0}'.format(self._altmetric_api_config.api_base_command)

        if self._altmetric_api_config.api_requested_item_id_type:
            url = url + '/{0}'.format(self._altmetric_api_config.api_requested_item_id_type)

        if self._doi:
            url = url + '/{0}'.format(self._doi)

        if self._altmetric_api_config.api_key:
            url = url + '?key={0}'.format(self._altmetric_api_config.api_key)

        return url
