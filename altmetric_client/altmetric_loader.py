from altmetric_client.altmetric import Altmetric
from altmetric_client.altmetric_score import AltmetricScore
from altmetric_client.altmetric_score_context import AltmetricScoreContext
from altmetric_client.altmetric_score_history import AltmetricScoreHistory
from altmetric_client.mention import Mention
from altmetric_client.author_manager import AuthorManager
from altmetric_client.author import Author
from altmetric_client.subject import Subject
from altmetric_client.user_demographics import UserDemographics
from altmetric_client.geo_demographics import GeoDemographics

import time

class AltmetricLoader:

    """Parses out the Altmetric JSON in a manner that we retain some control over.
    I could probably have just generated some sort of local object from the JSON automagically, but
    coding this by hand gave me a chance to have a proper look at the data being returned, and
    wrap a decent set of tests around the whole process, too (which might come in handy if someone
    changes the Altmetric API in a way that breaks what we're trying to do with it)."""

    def __init__(self):

        self.__author_manager = None
        self.__result = None


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

        self.__result = Altmetric()

        """Takes a data object based upon some Altmetric JSON and writes the fields we want 
        to a local Altmetric object"""

        self.__result.altmetric_id = str(data["altmetric_id"])
        self.__result.altmetric_score = float(data["altmetric_score"]["score"])
        self.__result.total_mentions = data["counts"]["total"]["posts_count"]

        self._load_citation_data(data["citation"])

        self._load_scores(data["altmetric_score"])

        self._load_demographics(data["demographics"])

        self._load_mentions(data["posts"])

        return self.__result

    def _load_citation_data(self, citation_data):

        self.__result.article_title = self._strip_breaks_and_spaces(citation_data["title"])
        self.__result.doi = str(citation_data['doi'])
        self.__result.journal_title = citation_data["journal"]

        if 'altmetric_jid' not in citation_data:

            self.__result.altmetric_journal_id = 'NA'

        else:

            self.__result.altmetric_journal_id = citation_data["altmetric_jid"]

        self.__result.print_publication_date = citation_data["pubdate"]
        self.__result.first_seen_on_date = citation_data["first_seen_on"]

        if 'authors' not in citation_data:

            self.__result.first_author = 'NA'

        else:

            self.__result.first_author = self._find_first_author(citation_data["authors"])

        if 'startpage' not in citation_data:
            self.__result.page_starts = 'NA'
        else:
            self.__result.page_starts = citation_data['startpage']

        if 'endpage' not in citation_data:
            self.__result.page_ends = 'NA'
        else:
            self.__result.page_ends = citation_data['endpage']

        if 'volume' not in citation_data:
            self.__result.journal_volume = 'NA'
        else:
            self.__result.journal_volume = citation_data['volume']

        if 'issue' not in citation_data:
            self.__result.journal_issue = 'NA'
        else:
            self.__result.journal_issue = citation_data['issue']

        if 'last_mentioned_on' not in citation_data:
            self.__result.last_mentioned_date = 'NA'
        else:
            self.__result.last_mentioned_date = time.strftime('%Y-%m-%dT%H:%M',
                                                              time.localtime(citation_data['last_mentioned_on']))

        if 'pdf_url' not in citation_data:
            self.__result.pdf_url = "NA"
        else:
            self.__result.pdf_url = citation_data['pdf_url']

        if 'publisher' not in citation_data:
            self.__result.publisher = 'NA'
        else:
            self.__result.publisher = citation_data['publisher']

        if 'type' not in citation_data:
            self.__result.type = 'NA'
        else:
            self.__result.type = citation_data['type']

        if 'uri' not in citation_data:
            self.__result.uri = 'NA'
        else:
            self.__result.uri = citation_data['uri']

        if 'mendeley_url' not in citation_data:
            self.__result.mendeley_url = 'NA'
        else:
            self.__result.mendeley_url = citation_data['mendeley_url']

        self._load_subjects(citation_data)

    def _load_scores(self, scores_data):

        scores = AltmetricScore()
        scores.doi = self.__result.doi
        scores.total_score = scores_data["score"]

        scores.score_history = self._load_score_history(scores_data["score_history"])

        context_data = scores_data["context_for_score"]

        scores.context_all = self._load_score_context(context_data["all"])
        scores.context_similar_age_three_months = self._load_score_context(context_data["similar_age_3m"])
        scores.context_this_journal = self._load_score_context(context_data["this_journal"])
        scores.context_similar_age_this_journal_three_months = self._load_score_context(context_data["similar_age_this_journal_3m"])

        self.__result.scores = scores

    def _load_score_history(self, score_history_data):

        score_history = AltmetricScoreHistory()
        score_history.last_one_year = score_history_data["1y"]
        score_history.last_six_months = score_history_data["6m"]
        score_history.last_three_months = score_history_data["3m"]
        score_history.last_one_month = score_history_data["1m"]
        score_history.last_one_week = score_history_data["1w"]
        score_history.last_six_days = score_history_data["6d"]
        score_history.last_five_days = score_history_data["5d"]
        score_history.last_four_days = score_history_data["4d"]
        score_history.last_three_days = score_history_data["3d"]
        score_history.last_two_days = score_history_data["2d"]
        score_history.last_one_day = score_history_data["1d"]

        return score_history

    def _load_score_context(self, context_data):

        context = AltmetricScoreContext()
        context.total_number_of_other_articles = context_data["total_number_of_other_articles"]
        context.mean = context_data["mean"]
        context.rank = context_data["rank"]
        context.this_scored_higher_than_pct = context_data["this_scored_higher_than_pct"]
        context.this_scored_higher_than = context_data["this_scored_higher_than"]
        context.rank_type = context_data["rank_type"]
        context.percentile = context_data["percentile"]

        return context

    def _load_subjects(self, citation_data):

        if 'subjects' in citation_data:

            for subject in citation_data['subjects']:

                altmetric_subject = Subject()
                altmetric_subject.doi = self.__result.doi
                altmetric_subject.scheme = 'altmetric'
                altmetric_subject.name = subject
                self.__result.add_subject(altmetric_subject)

        if 'scopus_subjects' in citation_data:

            for subject in citation_data['scopus_subjects']:

                scopus_subject = Subject()
                scopus_subject.doi = self.__result.doi
                scopus_subject.scheme = 'scopus'
                scopus_subject.name = subject
                self.__result.add_subject(scopus_subject)

        if 'publisher_subjects' in citation_data:

            for subject in citation_data['publisher_subjects']:

                publisher_subject = Subject()
                publisher_subject.doi = self.__result.doi
                publisher_subject.scheme = subject['scheme']
                publisher_subject.name = subject['name']
                self.__result.add_subject(publisher_subject)

    def _load_demographics(self, demographics_data):

        if 'poster_types' not in demographics_data:

            print("Article with DOI {0} did not have poster types demographic data."
                  .format(self.__result.doi))
        else:

            self._load_poster_types(demographics_data['poster_types'])

        if 'users' not in demographics_data:

            print("Article with DOI {0} did not have user demographics data."
                  .format(self.__result.doi))
        else:

            self._load_user_demographics(demographics_data['users'])

        if 'geo' not in demographics_data:

            print("Article with DOI {0} did not have geo demographics data."
                  .format(self.__result.doi))

        else:

            self._load_geo_demographics(demographics_data['geo'])

    def _load_poster_types(self, poster_types_data):

        for poster_type in poster_types_data:

            altmetric_user_demographic = UserDemographics()
            altmetric_user_demographic.source = 'altmetric'
            altmetric_user_demographic.group_type = 'poster_types'
            altmetric_user_demographic.group_value = poster_type
            altmetric_user_demographic.total = poster_types_data[poster_type]
            self.__result.add_user_demographics(altmetric_user_demographic)

    def _load_user_demographics(self, user_demographics_data):

        if 'twitter' not in user_demographics_data:
            print('Article with DOI {0} did not have user demographics data from Twitter.'.format(self.__result.doi))
        else:

            twitter_demographics = user_demographics_data['twitter']

            for cohort in twitter_demographics['cohorts']:

                twitter_cohort_demographics = UserDemographics()
                twitter_cohort_demographics.doi = self.__result.doi
                twitter_cohort_demographics.source = 'twitter'
                twitter_cohort_demographics.group_type = 'cohort'
                twitter_cohort_demographics.group_value = cohort
                twitter_cohort_demographics.total = twitter_demographics['cohorts'][cohort]
                self.__result.add_user_demographics(twitter_cohort_demographics)

        if 'mendeley' not in user_demographics_data:
            print('Article with DOI {0} did not have user demographics data from Mendeley.'.format(self.__result.doi))
        else:

            mendeley_demographics = user_demographics_data['mendeley']

            for mendeley_status_demographic in mendeley_demographics['by_status']:

                mendeley_by_status_demographic = UserDemographics()
                mendeley_by_status_demographic.doi = self.__result.doi
                mendeley_by_status_demographic.source = 'mendeley'
                mendeley_by_status_demographic.group_type = 'by_status'
                mendeley_by_status_demographic.group_value = mendeley_status_demographic
                mendeley_by_status_demographic.total = mendeley_demographics['by_status'][mendeley_status_demographic]
                self.__result.add_user_demographics(mendeley_by_status_demographic)

            for mendeley_discipline_demographic in mendeley_demographics['by_discipline']:

                mendeley_by_discipline_demographic = UserDemographics()
                mendeley_by_discipline_demographic.doi = self.__result.doi
                mendeley_by_discipline_demographic.source = 'mendeley'
                mendeley_by_discipline_demographic.group_type = 'by_discipline'
                mendeley_by_discipline_demographic.group_value = mendeley_discipline_demographic
                mendeley_by_discipline_demographic.total = mendeley_demographics['by_discipline'][mendeley_discipline_demographic]
                self.__result.add_user_demographics(mendeley_by_discipline_demographic)

    def _load_geo_demographics(self, geo_demographics_data):

        if 'twitter' not in geo_demographics_data:
            print('Article with DOI {0} did not have geo demographics data from Twitter.'.format(self.__result.doi))

        else:

            twitter_geo_demographics = geo_demographics_data['twitter']

            for twitter_geo_demographic_data in twitter_geo_demographics:

                twitter_geo_demographic = GeoDemographics()
                twitter_geo_demographic.doi = self.__result.doi
                twitter_geo_demographic.source = 'twitter'
                twitter_geo_demographic.country_code = twitter_geo_demographic_data
                twitter_geo_demographic.total = twitter_geo_demographics[twitter_geo_demographic_data]
                self.__result.add_geo_demographics(twitter_geo_demographic)

        if 'mendeley' not in geo_demographics_data:
            print('Article with DOI {0} did not have geo demographics data from Mendeley.'.format(self.__result.doi))
        else:
            mendeley_geo_demographics = geo_demographics_data['mendeley']

            for mendeley_geo_demographic_data in mendeley_geo_demographics:

                mendeley_geo_demographic = GeoDemographics()
                mendeley_geo_demographic.doi = self.__result.doi
                mendeley_geo_demographic.source = 'mendeley'
                mendeley_geo_demographic.country_code = mendeley_geo_demographic_data
                mendeley_geo_demographic.total = mendeley_geo_demographics[mendeley_geo_demographic_data]
                self.__result.add_geo_demographics(mendeley_geo_demographic)

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

    def _load_mentions(self, posts_data):

        for source in posts_data:

            try:

                for altmetric_mention in posts_data[source]:

                    mention = Mention()

                    if 'author' not in altmetric_mention:

                        mention.author_id = 'NA'

                    else:

                        mention_author = self._parse_author(altmetric_mention['author'], source)
                        mention.author_id = self.__author_manager.add_author(mention_author)

                    mention.source = str(source)
                    mention.related_article_doi = self.__result.doi
                    mention.url = altmetric_mention['url']
                    mention.date_posted = altmetric_mention['posted_on']
                    self.__result.add_mention(mention)

            except:

                print("An error occurred when processing mentions for source: {0}, article DOI: {1}".format(str(source),
                        self.__result.doi))

    def _parse_author(self, author_data, source):

        author = Author()

        author.source = source

        if 'name' not in author_data:
            author.name = 'NA'
        else:
            author.name = self._strip_breaks_and_spaces(author_data['name'])

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
            author.description = self._strip_breaks_and_spaces(author_data['description'])

        if 'id_on_source' not in author_data:
            author.id_on_source = 'NA'
        else:
            author.id_on_source = author_data['id_on_source']

        if 'followers' not in author_data:
            author.followers = 0
        else:
            author.followers = int(author_data['followers'])

        return author
