from altmetric_client.mention import Mention
from altmetric_client.subject import Subject
from altmetric_client.user_demographics import UserDemographics

class Altmetric:

    def __init__(self):

        self.__doi = None
        self.__altmetric_id = None
        self.__altmetric_score = None
        self.__article_title = None
        self.__journal_title = None
        self.__journal_volume = None
        self.__journal_issue = None
        self.__altmetric_journal_id = None
        self.__total_mentions = None
        self.__print_publication_date = None
        self.__first_seen_on_date = None
        self.__first_author = None
        self.__page_starts = None
        self.__page_ends = None
        self.__last_mentioned_date = None
        self.__pdf_url = None
        self.__publisher = None
        self.__type = None
        self.__uri = None
        self.__mendeley_url = None
        self.__poster_type_members_of_public_count = None
        self.__poster_type_researcher_count = None
        self.__poster_type_practitioner_count = None
        self.__poster_type_science_communicator_count = None

        self.__mentions = []
        self.__subjects = []
        self.__user_demographics = []

    @property
    def doi(self):
        return self.__doi

    @doi.setter
    def doi(self, doi):
        self.__doi = doi

    @property
    def altmetric_id(self):
        return self.__altmetric_id

    @altmetric_id.setter
    def altmetric_id(self, altmetric_id):
        self.__altmetric_id = altmetric_id

    @property
    def altmetric_score(self):
        return self.__altmetric_score

    @altmetric_score.setter
    def altmetric_score(self, altmetric_score):
        self.__altmetric_score = altmetric_score

    @property
    def article_title(self):
        return self.__article_title

    @article_title.setter
    def article_title(self, article_title):
        self.__article_title = article_title

    @property
    def journal_title(self):
        return self.__journal_title

    @journal_title.setter
    def journal_title(self, journal_title):
        self.__journal_title = journal_title

    @property
    def journal_volume(self):
        return self.__journal_volume

    @journal_volume.setter
    def journal_volume(self, journal_volume):
        self.__journal_volume = journal_volume

    @property
    def journal_issue(self):
        return self.__journal_issue

    @journal_issue.setter
    def journal_issue(self, journal_issue):
        self.__journal_issue = journal_issue

    @property
    def altmetric_journal_id(self):
        return self.__altmetric_journal_id

    @altmetric_journal_id.setter
    def altmetric_journal_id(self, altmetric_journal_id):
        self.__altmetric_journal_id = altmetric_journal_id

    @property
    def total_mentions(self):
        return self.__total_mentions

    @total_mentions.setter
    def total_mentions(self, total_mentions):
        self.__total_mentions = total_mentions

    @property
    def print_publication_date(self):
        return self.__print_publication_date

    @print_publication_date.setter
    def print_publication_date(self, print_publication_date):
        self.__print_publication_date = print_publication_date

    @property
    def first_seen_on_date(self):
        return self.__first_seen_on_date

    @first_seen_on_date.setter
    def first_seen_on_date(self, first_seen_on_date):
        self.__first_seen_on_date = first_seen_on_date

    @property
    def first_author(self):
        return self.__first_author

    @first_author.setter
    def first_author(self, authors):
        self.__first_author = authors

    @property
    def page_starts(self):
        return self.__page_starts

    @page_starts.setter
    def page_starts(self, page_starts):
        self.__page_starts = page_starts

    @property
    def page_ends(self):
        return self.__page_ends

    @page_ends.setter
    def page_ends(self, page_ends):
        self.__page_ends = page_ends

    @property
    def last_mentioned_date(self):
        return self.__last_mentioned_date

    @last_mentioned_date.setter
    def last_mentioned_date(self, last_mentioned_date):
        self.__last_mentioned_date = last_mentioned_date

    @property
    def pdf_url(self):
        return self.__pdf_url

    @pdf_url.setter
    def pdf_url(self, pdf_url):
        self.__pdf_url = pdf_url

    @property
    def publisher(self):
        return self.__publisher

    @publisher.setter
    def publisher(self, publisher):
        self.__publisher = publisher

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type):
        self.__type = type

    @property
    def uri(self):
        return self.__uri

    @uri.setter
    def uri(self, uri):
        self.__uri = uri

    @property
    def mendeley_url(self):
        return self.__mendeley_url

    @mendeley_url.setter
    def mendeley_url(self, mendeley_url):
        self.__mendeley_url = mendeley_url
        
    @property
    def poster_type_members_of_public_count(self):
        return self.__poster_type_members_of_public_count
    
    @poster_type_members_of_public_count.setter
    def poster_type_members_of_public_count(self, poster_type_members_of_public_count):
        self.__poster_type_members_of_public_count = poster_type_members_of_public_count

    @property
    def poster_type_researcher_count(self):
        return self.__poster_type_researcher_count

    @poster_type_researcher_count.setter
    def poster_type_researcher_count(self, poster_type_researcher_count):
        self.__poster_type_researcher_count = poster_type_researcher_count

    @property
    def poster_type_practitioner_count(self):
        return self.__poster_type_practitioner_count

    @poster_type_practitioner_count.setter
    def poster_type_practitioner_count(self, poster_type_practitioner_count):
        self.__poster_type_practitioner_count = poster_type_practitioner_count

    @property
    def poster_type_science_communicator_count(self):
        return self.__poster_type_science_communicator_count

    @poster_type_science_communicator_count.setter
    def poster_type_science_communicator_count(self, poster_type_science_communicator_count):
        self.__poster_type_science_communicator_count = poster_type_science_communicator_count

    @property
    def mentions(self):
        return self.__mentions

    def add_mention(self, mention: Mention):
        self.__mentions.append(mention)

    @property
    def subjects(self):
        return self.__subjects

    def add_subject(self, subject: Subject):
        self.__subjects.append(subject)

    @property
    def user_demographics(self):
        return self.__user_demographics

    def add_user_demographics(self, user_demographics: UserDemographics):
        self.__user_demographics.append(user_demographics)


