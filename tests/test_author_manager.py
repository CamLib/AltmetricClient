from altmetric_client.author_manager import AuthorManager
from altmetric_client.author import Author

class TestAuthorManager:

    def setup_method(self):

        self.test_author_manager = AuthorManager()

        self.test_twitter_author1 = Author()
        self.test_twitter_author1.name = "Test Author 1"
        self.test_twitter_author1.source = 'twitter'
        self.test_twitter_author1.id_on_source = 'testauthor1'

        self.test_twitter_author2 = Author()
        self.test_twitter_author2.name = "Test Author 2"
        self.test_twitter_author2.source = 'twitter'
        self.test_twitter_author2.id_on_source = 'testauthor2'


    def teardown_method(self):

        self.test_author_manager = None

    def test_single_twitter_author_returns_internal_author_id(self):

        assert self.test_author_manager.add_author(self.test_twitter_author1) == 'twitter1'

    def test_adding_single_author_adds_author_to_list(self):

        author_id = self.test_author_manager.add_author(self.test_twitter_author1)
        result = self.test_author_manager.authors
        assert result[0].name == 'Test Author 1'

    def test_adding_second_twitter_author_returns_correct_id(self):

        author_id = self.test_author_manager.add_author(self.test_twitter_author1)

        assert self.test_author_manager.add_author(self.test_twitter_author2) == 'twitter2'

    def test_second_twitter_author_has_correct_id_in_authors_list(self):

        author_id = self.test_author_manager.add_author(self.test_twitter_author1)
        author_id2 = self.test_author_manager.add_author(self.test_twitter_author2)

        result = self.test_author_manager.authors

        assert result[1].author_id == 'twitter2'

    def test_adding_author_again_returns_original_id(self):

        author_id = self.test_author_manager.add_author(self.test_twitter_author1)
        author_id2 = self.test_author_manager.add_author(self.test_twitter_author2)
        assert self.test_author_manager.add_author(self.test_twitter_author1) == "twitter1"

    def test_adding_author_again_returns_list_of_two_authors(self):

        author_id = self.test_author_manager.add_author(self.test_twitter_author1)
        author_id2 = self.test_author_manager.add_author(self.test_twitter_author2)
        author_id3 = self.test_author_manager.add_author(self.test_twitter_author1)

        result = self.test_author_manager.authors

        assert len(result) == 2

    def test_adding_author_different_source_different_id_on_source(self):

        author_id = self.test_author_manager.add_author(self.test_twitter_author1)
        author_id2 = self.test_author_manager.add_author(self.test_twitter_author2)

        different_source_author = Author()
        different_source_author.name = "Test Author 3"
        different_source_author.source = 'facebook'
        different_source_author.id_on_source = 'testauthor3'

        author_id3 = self.test_author_manager.add_author(different_source_author)

        result = self.test_author_manager.authors

        assert result[2].author_id == 'facebook3'

    def test_adding_author_different_source_same_id_on_source(self):

        author_id = self.test_author_manager.add_author(self.test_twitter_author1)
        author_id2 = self.test_author_manager.add_author(self.test_twitter_author2)

        different_source_author = Author()
        different_source_author.name = "Test Author 1"
        different_source_author.source = 'facebook'
        different_source_author.id_on_source = 'testauthor1'

        author_id3 = self.test_author_manager.add_author(different_source_author)

        result = self.test_author_manager.authors

        assert result[2].author_id == 'facebook3'

    def test_adding_author_googleplus_source(self):

        url_id_field_author = Author()
        url_id_field_author.name = "Test Author 1"
        url_id_field_author.source = 'googleplus'
        url_id_field_author.id_on_source = 'testauthor1'

        author_id3 = self.test_author_manager.add_author(url_id_field_author)

        result = self.test_author_manager.authors

        assert result[0].author_id == 'googleplus1'

    def test_adding_author_reddit_source(self):

        url_id_field_author = Author()
        url_id_field_author.name = "Test Author 1"
        url_id_field_author.source = 'reddit'
        url_id_field_author.id_on_source = 'testauthor1'

        author_id3 = self.test_author_manager.add_author(url_id_field_author)

        result = self.test_author_manager.authors

        assert result[0].author_id == 'reddit1'

    def test_adding_author_video_source(self):

        url_id_field_author = Author()
        url_id_field_author.name = "Test Author 1"
        url_id_field_author.source = 'video'
        url_id_field_author.id_on_source = 'testauthor1'

        author_id3 = self.test_author_manager.add_author(url_id_field_author)

        result = self.test_author_manager.authors

        assert result[0].author_id == 'video1'

    def test_adding_author_q_and_a_source(self):

        url_id_field_author = Author()
        url_id_field_author.name = "Test Author 1"
        url_id_field_author.source = 'q&a'
        url_id_field_author.id_on_source = 'testauthor1'

        author_id3 = self.test_author_manager.add_author(url_id_field_author)

        result = self.test_author_manager.authors

        assert result[0].author_id == 'q&a1'

    def test_adding_author_weibo_source(self):

        url_id_field_author = Author()
        url_id_field_author.name = "Test Author 1"
        url_id_field_author.source = 'weibo'
        url_id_field_author.id_on_source = 'testauthor1'

        author_id3 = self.test_author_manager.add_author(url_id_field_author)

        result = self.test_author_manager.authors

        assert result[0].author_id == 'weibo1'

    def test_adding_author_peer_review_source(self):

        url_id_field_author = Author()
        url_id_field_author.name = "Test Author 1"
        url_id_field_author.source = 'peer_reviews'
        url_id_field_author.id_on_source = 'testauthor1'

        author_id3 = self.test_author_manager.add_author(url_id_field_author)

        result = self.test_author_manager.authors

        assert result[0].author_id == 'peer_reviews1'


    def test_adding_author_blogs_source(self):

        url_id_field_author = Author()
        url_id_field_author.name = "Test Author 1"
        url_id_field_author.source = 'blogs'
        url_id_field_author.url = 'http://testauthor1.com'

        author_id3 = self.test_author_manager.add_author(url_id_field_author)

        result = self.test_author_manager.authors

        assert result[0].author_id == 'blogs1'

    def test_adding_author_news_source(self):

        url_id_field_author = Author()
        url_id_field_author.name = "Test Author 1"
        url_id_field_author.source = 'news'
        url_id_field_author.url = 'http://testauthor1.com'

        author_id3 = self.test_author_manager.add_author(url_id_field_author)

        result = self.test_author_manager.authors

        assert result[0].author_id == 'news1'

    def test_adding_author_wikipedia_source(self):

        url_id_field_author = Author()
        url_id_field_author.name = "Test Author 1"
        url_id_field_author.source = 'wikipedia'
        url_id_field_author.url = 'http://testauthor1.com'

        author_id3 = self.test_author_manager.add_author(url_id_field_author)

        result = self.test_author_manager.authors

        assert result[0].author_id == 'wikipedia1'

    def test_adding_author_misc_source(self):

        url_id_field_author = Author()
        url_id_field_author.name = "Test Author 1"
        url_id_field_author.source = 'misc'

        author_id3 = self.test_author_manager.add_author(url_id_field_author)

        result = self.test_author_manager.authors

        assert result[0].author_id == 'misc1'

    def test_adding_author_pinterest_source(self):

        url_id_field_author = Author()
        url_id_field_author.name = "Test Author 1"
        url_id_field_author.source = 'pinterest'

        author_id3 = self.test_author_manager.add_author(url_id_field_author)

        result = self.test_author_manager.authors

        assert result[0].author_id == 'pinterest1'

    def test_adding_author_linkedin_source(self):

        url_id_field_author = Author()
        url_id_field_author.name = "Test Author 1"
        url_id_field_author.source = 'linkedin'

        author_id3 = self.test_author_manager.add_author(url_id_field_author)

        result = self.test_author_manager.authors

        assert result[0].author_id == 'linkedin1'

    def test_adding_author_policy_source(self):

        url_id_field_author = Author()
        url_id_field_author.name = "Test Author 1"
        url_id_field_author.source = 'policy'

        author_id3 = self.test_author_manager.add_author(url_id_field_author)

        result = self.test_author_manager.authors

        assert result[0].author_id == 'policy1'

    def test_adding_author_f1000_source(self):

        url_id_field_author = Author()
        url_id_field_author.name = "Test Author 1"
        url_id_field_author.source = 'f1000'

        assert self.test_author_manager.add_author(url_id_field_author) == 'NA'

    def test_adding_author_unanticipated_source_returns_NA(self):

        url_id_field_author = Author()
        url_id_field_author.name = "Test Author 1"
        url_id_field_author.source = 'unanticipated'

        assert self.test_author_manager.add_author(url_id_field_author) == 'NA'

    def test_adding_author_unanticipated_source_prints_the_source_name(self, capfd):

        url_id_field_author = Author()
        url_id_field_author.name = "Test Author 1"
        url_id_field_author.source = 'unanticipated'

        result = self.test_author_manager.add_author(url_id_field_author) == 'NA'

        out, err = capfd.readouterr()
        assert out == 'Author had unanticipated source: unanticipated\n'
