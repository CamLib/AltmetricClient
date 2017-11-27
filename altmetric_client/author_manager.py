from altmetric_client.author import Author

class AuthorManager:

    def __init__(self):

        self.__id_counter = 0
        self.__authors = []
        self.__author_field_rules = dict(twitter='id_on_source',
                                         facebook='id_on_source',
                                         blogs='url')

    @property
    def authors(self):
        return self.__authors

    def add_author(self, author: Author):

        existing_author = None

        if self.__author_field_rules[author.source] == 'id_on_source':

            existing_author = [existing
                               for existing in self.__authors
                               if existing.source == author.source
                               and existing.id_on_source == author.id_on_source]

        elif self.__author_field_rules[author.source] == 'url':

            existing_author = [existing
                               for existing in self.__authors
                               if existing.source == author.source
                               and existing.url == author.url]

        if len(existing_author) == 1:

            return existing_author[0].author_id

        elif len(existing_author) == 0:

            self.__id_counter += 1
            author.author_id = "{0}{1}".format(author.source, self.__id_counter)
            self.__authors.append(author)

        else:

            print("This author has already been added to the list more than once for some reason...")

        return author.author_id