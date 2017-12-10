from altmetric_client.output_writer_csv.csv_writer_base import CSVWriterBase
from csv import DictWriter

class CSVWriterAuthor(CSVWriterBase):

    def __init__(self,
                 output_file_name=None,
                 output_directory_name=None,
                 authors_list=None):

        CSVWriterBase.__init__(self, output_file_name, output_directory_name)
        self.__authors_list = authors_list

    @property
    def authors_list(self):
        return self.__authors_list

    @authors_list.setter
    def authors_list(self, authors_list):
        self.__authors_list = authors_list

    def write_authors(self):

        output_file_path = '{0}{1}'.format(self.output_directory_name, self.output_file_name)

        write_mode = self._get_write_mode(output_file_path)

        fieldnames = ['author_id',
                      'author_name',
                      'author_source',
                      'author_url',
                      'author_id_on_source',
                      'author_description',
                      'author_image_url',
                      'author_follower_count']

        try:

            with open(output_file_path, write_mode) as output_csv:

                output_writer = DictWriter(output_csv, fieldnames=fieldnames)

                if write_mode == 'w':
                    output_writer.writeheader()

                for author in self.authors_list:

                    output_dict = dict(author_id=author.author_id,
                                       author_name=author.name,
                                       author_source=author.source,
                                       author_url=author.url,
                                       author_id_on_source=author.id_on_source,
                                       author_description=author.description,
                                       author_image_url=author.image_url,
                                       author_follower_count=author.followers)

                    output_writer.writerow(output_dict)

        except:

            print('Something totally unexpected happened when trying to write to an Authors CSV file')
            print('The writer was setup to write to a file called {0}{1}'.format(self.output_directory_name,
                                                                                 self.output_file_name))
            if write_mode == 'a':
                print('The writer thought this file existed and was trying to append to it.')
            elif write_mode == 'w':

                print('The writer thought this was a brand new file and was trying to create it.')
            else:
                print('The writer could not determine whether or not the file existed.')