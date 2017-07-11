from altmetric_client.altmetric import Altmetric

class AltmetricLoader:

    def parse_result(self, data=None):

        result = Altmetric()
        result.journal_title = data["citation"]["journal"]
        result.altmetric_score = float(data["altmetric_score"]["score"])

        return result
