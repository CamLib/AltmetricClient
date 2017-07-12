import configparser
from altmetric_client.altmetric_api_config import AltmetricAPIConfig

class AltmetricClient:

    def run(self):

        config_data = configparser.ConfigParser()

        try:
            with open('config.ini') as config_file:
                config_data.read_file(config_file)
        except:
            print('There was an error reading the config.ini file. See the project README.md for details of how to set one up.')
            quit()

        api_config = self._load_config(config_data)

        # Printouts added for 'by eye' testing.
        # We don't want to push the config file into GitHub, so Unit Testing can't happen

        print("Base URI: {0}".format(api_config.api_base_uri))
        print("API Version: {0}".format(api_config.api_version))
        print("API Base command: {0}".format(api_config.api_base_command))
        print("API Requested Item Id Type: {0}".format(api_config.api_requested_item_id_type))
        print("API Key: {0}".format(api_config.api_key))

        # Now pass the config into the constructor of a AltmetricDataFetcher class


    def _load_config(self, config_data):

        api_config = AltmetricAPIConfig()

        try:
            api_config.api_base_uri = config_data['api.altmetric.com']['APIBaseURI']
        except:
            print('The APIBaseURI field has not been added to the config.ini file properly. See the project README.md for details about how to set this up.')
            quit()

        try:
            api_config.api_version = config_data['api.altmetric.com']['APIVersion']
        except:
            print('The APIVersion field has not been added to the config.ini file properly. See the project README.md for details about how to set this up.')
            quit()

        try:
            api_config.api_base_command = config_data['api.altmetric.com']['APIBaseCommand']
        except:
            print('The APIBaseCommand field has not been added to the config.ini file properly. See the project README.md for details about how to set this up.')
            quit()

        try:
            api_config.api_requested_item_id_type = config_data['api.altmetric.com']['APIRequestedItemIdType']
        except:
            print('The APIRequestedItemIdType field has not been added to the config.ini file properly. See the project README.md for details about how to set this up.')
            quit()

        try:
            api_config.api_key = config_data['api.altmetric.com']['APIKey']
        except:
            print('The APIKey field has not been added to the config.ini file properly. See the project README.md for details about how to set this up.')
            quit()

        return api_config

if __name__ == "__main__":

    AltmetricClient().run()