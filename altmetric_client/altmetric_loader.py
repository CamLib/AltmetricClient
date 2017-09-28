from altmetric_client.altmetric import Altmetric

class AltmetricLoader:

    # Need a way of testing all these answers for 'None' and returning 'Not found' or something

    def parse_result(self, data=None):

        result = Altmetric()
        result.altmetric_id = str(data["altmetric_id"])
        result.altmetric_score = float(data["altmetric_score"]["score"])
        result.article_title = data["citation"]["title"]
        result.journal_title = data["citation"]["journal"]
        result.altmetric_journal_id = data["citation"]["altmetric_jid"]
        result.total_mentions = data["counts"]["total"]["posts_count"]
        result.print_publication_date = data["citation"]["pubdate"]
        result.first_seen_on_date = data["citation"]["first_seen_on"]



        return result
