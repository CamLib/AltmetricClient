from altmetric_client.author import Author

class AuthorManager:

    '''This class is still a bit of a hack. At least it uses reflection now (reflection in Python seems to be
    as easy as the rest of it). However, it would be nice to move the field rules dictionary to the config.ini
    and pass them in, so adding new rules about authors from other sources as yet unknown is just a matter of
    changing the config. (Unless the identifying property is a property that none of the current authors have,
    of course...)'''

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
                                            policy='image_url',
                                            f1000='NA')

    @property
    def authors(self):
        return self.__authors

    def add_author(self, author: Author):

        '''One of the sources quite handily has an ampersand in it, which means
        it can't be used as the key in a dictionary.'''

        try:

            rules_key = str(author.source).replace('&', '')
            identifying_property = self.__author_id_field_rules[rules_key]

            if identifying_property == 'NA':

                return 'NA'

            else:

                existing_author = [existing
                                   for existing in self.__authors
                                   if existing.source == author.source
                                   and getattr(existing, identifying_property) == getattr(author, identifying_property)]

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
