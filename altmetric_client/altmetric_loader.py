from altmetric_client.altmetric import Altmetric

class AltmetricLoader:

    """Parses out the Altmetric JSON in a manner that we retain some control over.
    I could probably have just generated some sort of local object from the JSON automagically, but
    coding this by hand gave me a chance to have a proper look at the data being returned, and
    wrap a decent set of tests around the whole process, too (which might come in handy if someone
    changes the Altmetric API in a way that breaks what we're trying to do with it)."""

    def parse_result(self, data=None):

        """Takes a data object based upon some Altmetric JSON and writes the fields we want 
        to a local Altmetric object"""

        result = Altmetric()
        result.altmetric_id = str(data["altmetric_id"])
        result.altmetric_score = float(data["altmetric_score"]["score"])

        result.article_title = self._strip_breaks_and_spaces(data["citation"]["title"])
        result.journal_title = data["citation"]["journal"]

        if 'altmetric_jid' not in data["citation"]:

            result.altmetric_journal_id = 'N/A'

        else:

            result.altmetric_journal_id = data["citation"]["altmetric_jid"]

        result.total_mentions = data["counts"]["total"]["posts_count"]
        result.print_publication_date = data["citation"]["pubdate"]
        result.first_seen_on_date = data["citation"]["first_seen_on"]

        if 'authors' not in data["citation"]:

            result.first_author = 'N/A'

        else:
            result.first_author = data["citation"]["authors"][0]

        return result

    def _strip_breaks_and_spaces(self, broken_string):

        """
        Strips all the breaks and extra white spaces out of a given string
        :rtype: str
        """
        return ' '.join(str(broken_string).split())