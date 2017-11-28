from altmetric_client.author import Author

class AuthorManager:

    '''This class is a hack currently. I'd like it to be fully extensible with the author id
    rules in the config. (If this was C# I could do so with reflection - I suspect I'll be able
    to do something similar with Python, but I don't have time to find out right now).'''

    def __init__(self):

        self.__id_counter = 0
        self.__authors = []
        self.__author_id_field_rules = dict(twitter='id_on_source',
                                            facebook='id_on_source',
                                            googleplus='id_on_source',
                                            reddit='id_on_source',
                                            video='id_on_source',
                                            qa='id_on_source',
                                            weibo='id_on_source',
                                            peer_reviews='id_on_source',
                                            blogs='url',
                                            news='url',
                                            wikipedia='url',
                                            misc='name',
                                            pinterest='name',
                                            linkedin='name',
                                            policy='name',
                                            f1000='NA')

    @property
    def authors(self):
        return self.__authors

    def add_author(self, author: Author):

        '''One of the sources quite handily has an ampersand in it, which means
        it can't be used as the key in a dictionary.'''

        existing_author = None
        rules_key = str(author.source).replace('&', '')

        try:

            if self.__author_id_field_rules[rules_key] == 'id_on_source':

                existing_author = [existing
                                   for existing in self.__authors
                                   if existing.source == author.source
                                   and existing.id_on_source == author.id_on_source]

            elif self.__author_id_field_rules[rules_key] == 'url':

                existing_author = [existing
                                   for existing in self.__authors
                                   if existing.source == author.source
                                   and existing.url == author.url]

            elif self.__author_id_field_rules[rules_key] == 'name':

                existing_author = [existing
                                   for existing in self.__authors
                                   if existing.source == author.source
                                   and existing.name == author.name]

            elif self.__author_id_field_rules[rules_key] == 'NA':

                return 'NA'

        except KeyError:

            print('Author had unanticipated source: {0}'.format(author.source))
            return 'NA'


        if len(existing_author) == 1:

            return existing_author[0].author_id

        elif len(existing_author) == 0:

            self.__id_counter += 1
            author.author_id = "{0}{1}".format(author.source, self.__id_counter)
            self.__authors.append(author)

        else:

            print("This author has already been added to the list more than once for some reason...")

        return author.author_id