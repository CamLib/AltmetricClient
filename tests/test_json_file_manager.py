from altmetric_client.json_file_manager import JSONFileManager

import json

class TestJSONFileManager:

    def setup_method(self):

        mentionsJsonFile = open("json_data/10Mentions.json")

        test_data = json.load(mentionsJsonFile)

        self.__test_json_file_manager = JSONFileManager("../files_out/")

        self.__test_json_file_manager.dump(test_data, "10.1108/LHT-06-2017-0122")

        mentionsJsonFile.close()

    def test_json_dumped_to_correct_file(self):

        with open("../files_out/10.1108---LHT-06-2017-0122.json") as result_file:

            result_data = json.load(result_file)

            assert result_data['altmetric_id'] == 584396

    def test_json_loads_file_from_directory(self):

        result_data = self.__test_json_file_manager.load("json_data", "10Mentions")

        assert result_data['altmetric_id'] == 584396
