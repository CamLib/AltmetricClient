from altmetric_client.altmetric import Altmetric
from altmetric_client.mention import Mention
from altmetric_client.author_manager import AuthorManager
from altmetric_client.author import Author

class AltmetricLoader:

    """Parses out the Altmetric JSON in a manner that we retain some control over.
    I could probably have just generated some sort of local object from the JSON automagically, but
    coding this by hand gave me a chance to have a proper look at the data being returned, and
    wrap a decent set of tests around the whole process, too (which might come in handy if someone
    changes the Altmetric API in a way that breaks what we're trying to do with it)."""


    def __init__(self):

        self.__author_manager = None

    @property
    def author_manager(self):
        return self.__author_manager

    @author_manager.setter
    def author_manager(self, author_manager: AuthorManager):
        self.__author_manager = author_manager

    @property
    def authors_list(self):
        return self.__author_manager.authors

    def parse_result(self, data=None):

        """Takes a data object based upon some Altmetric JSON and writes the fields we want 
        to a local Altmetric object"""

        result = Altmetric()
        result.altmetric_id = str(data["altmetric_id"])
        result.altmetric_score = float(data["altmetric_score"]["score"])

        result.article_title = self._strip_breaks_and_spaces(data["citation"]["title"])

        result.doi = str(data['citation']['doi'])

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

            result.first_author = self._find_first_author(data["citation"]["authors"])

        result = self._load_mentions(result, data["posts"])

        return result

    def _strip_breaks_and_spaces(self, broken_string):

        """
        Strips all the breaks and extra white spaces out of a given string
        :rtype: str
        """

        return ' '.join(str(broken_string).split())

    def _find_first_author(self, authors):

        """
        Checks for dirty data in the first author in the list. Issues 10 and 12
        describe more - there are missing first authors in the list, commas and carriage returns in the
        author data.
        :rtype: str
        """
        if len(authors) > 0:

            first_value = self._strip_breaks_and_spaces(str(authors[0]))

            if len(first_value) == 0 or first_value == ',':
                return self._strip_breaks_and_spaces(str(authors[1]))
            else:
                return first_value

    def _load_mentions(self, result:Altmetric, posts_data):

        for source in posts_data:

            try:

                for altmetric_mention in posts_data[source]:

                    mention = Mention()

                    if 'author' not in altmetric_mention:

                        mention.author_id = 'NA'

                    else:

                        mention_author = self.__parse_author(altmetric_mention['author'], source)
                        mention.author_id = self.__author_manager.add_author(mention_author)

                    mention.source = str(source)
                    mention.related_article_doi = result.doi
                    mention.url = altmetric_mention['url']
                    mention.date_posted = altmetric_mention['posted_on']
                    result.add_mention(mention)

            except:

                print("An error occurred when processing mentions for source: {0}, article DOI: {1}".format(str(source),
                        result.doi))

        return result

    def __parse_author(self, author_data, source):

        author = Author()

        author.source = source

        if 'name' not in author_data:
            author.name = 'NA'
        else:
            author.name = author_data['name']

        if 'url' not in author_data:
            author.url = 'NA'
        else:
            author.url = author_data['url']

        if 'image' not in author_data:
            author.image_url = 'NA'
        else:
            author.image_url = author_data['image']

        if 'description' not in author_data:
            author.description = 'NA'
        else:
            author.description = author_data['description']

        if 'id_on_source' not in author_data:
            author.id_on_source = 'NA'
        else:
            author.id_on_source = author_data['id_on_source']

        if 'followers' not in author_data:
            author.followers = 0
        else:
            author.followers = int(author_data['followers'])

        return author
