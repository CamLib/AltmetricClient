import requests
from altmetric_client.url_builder import URLBuilder

class AltmetricRequest:
    
    def __init__(self, url_builder:URLBuilder=None):

        self._url_builder = url_builder
        self._doi_to_request = None

    @property
    def url_builder(self):

        return self._url_builder

    @url_builder.setter
    def url_builder(self, url_builder):

        self._url_builder = url_builder

    @property
    def doi_to_request(self):

        return self._doi_to_request

    @doi_to_request.setter
    def doi_to_request(self, doi):

        self._doi_to_request = doi


    def request(self):

        if self.doi_to_request is None:

            print('A request to the Altmetric API was made without setting a DOI.')

        elif self.url_builder is None:

            print('A request to the Altmetric API was made without loading the config settings.')

        else:

            try:

                self.url_builder.doi = self.doi_to_request
                response = requests.get(self._url_builder.build_url())

                # The Altmetric API return errors as content strings

                if response.text == 'The API key you supplied was invalid.' or response.text == 'The API key you supplied was not recognized.':

                    print('Altmetric have denied access for the request for DOI {0}. The wrong API key may have been used in the configuration?'.format(self.doi_to_request))

                elif response.status_code == 404:

                    print('Altmetric have returned a 404 error for the request. This is most likely because of an error in your config file.')

                else:

                    return response.json()

            except:

                print('Something totally unexpected (i.e. not a 404 or 403) happened\
                 when requesting DOI {0}'.format(self.doi_to_request))

