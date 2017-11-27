from altmetric_client.altmetric_loader import AltmetricLoader
from altmetric_client.altmetric import Altmetric
from altmetric_client.mention import Mention

import json

class TestAltmetricLoaderMentions:

    def setup_method(self):

        self.mentionsJsonFile = open("json_data/101Mentions.json")

        test_data = json.load(self.mentionsJsonFile)

        test_altmetric_loader = AltmetricLoader()

        self.result = test_altmetric_loader.parse_result(test_data)

    def tear_down_method(self):

        self.mentionsJsonFile.close()

    def test_adding_mention_article_doi(self):

        test_mention = Mention()
        test_mention.related_article_doi = "/Test/DOI/1234"
        test_altmetric = Altmetric()
        test_altmetric.add_mention(test_mention)

        assert test_altmetric.mentions[0].related_article_doi == "/Test/DOI/1234"

    def test_adding_mention_url(self):

        test_mention = Mention()
        test_mention.url = "http://TestUrl.com"
        test_altmetric = Altmetric()
        test_altmetric.add_mention(test_mention)

        assert test_altmetric.mentions[0].url == "http://TestUrl.com"

    def test_adding_mention_source(self):

        test_mention = Mention()
        test_mention.source = "test_source"
        test_altmetric = Altmetric()
        test_altmetric.add_mention(test_mention)

        assert test_altmetric.mentions[0].source == "test_source"

    def test_adding_mention_date_posted(self):

        test_mention = Mention()
        test_mention.date_posted = "2013-12-02T14:02:15+00:00"
        test_altmetric = Altmetric()
        test_altmetric.add_mention(test_mention)

        assert test_altmetric.mentions[0].date_posted == "2013-12-02T14:02:15+00:00"

    def test_87_twitter_mentions_loaded(self):

        twitter_mentions = [mention for mention in self.result.mentions if mention.source == 'twitter']

        assert len(twitter_mentions) == 87

    def test_101Mentions_loaded(self):

        assert len(self.result.mentions) == 101

    def test_two_policy_mentions_loaded(self):

        policy_mentions = [mention for mention in self.result.mentions if mention.source == 'policy']

        assert len(policy_mentions) == 2

    def test_first_tweet_url_is_tweeflux(self):

        twitter_mentions = [mention for mention in self.result.mentions if mention.source == 'twitter']

        assert twitter_mentions[0].url == 'http://twitter.com/Tweeflux/status/414177303770316800'

    def test_first_facebook_mention_url_is_from_id_containing_53671(self):

        facebook_mentions = [mention for mention in self.result.mentions if mention.source == 'facebook']

        assert facebook_mentions[0].url == "https://www.facebook.com/536713609700448/posts/644781568893651"

    def test_first_googleplus_doi_matches_the_articles_doi(self):

        googleplus_mentions = [mention for mention in self.result.mentions if mention.source == 'googleplus']

        assert googleplus_mentions[0].related_article_doi == '10.1093/alcalc/agt174'

    def test_last_news_mention_date_posted_is_19_dec_2013(self):

        news_mentions = [mention for mention in self.result.mentions if mention.source == 'news']

        assert news_mentions[6].date_posted == '2013-12-19T22:06:42+00:00'

