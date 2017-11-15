from csv import DictWriter
from altmetric_client.mention import Mention
from altmetric_client.output_writer_csv.csv_writer_base import CSVWriterBase

class CSVWriterMention(CSVWriterBase):

    def __init__(self,
                 output_file_name=None,
                 output_directory_name=None,
                 mentions_list=None):

        CSVWriterBase.__init__(self, output_file_name, output_directory_name)
        self.__mentions_list = mentions_list

    @property
    def mentions_list(self):
        return self.__mentions_list

    @mentions_list.setter
    def mentions_list(self, mentions_list):
        self.__mentions_list = mentions_list

    def write_mentions(self):

        output_file_path = '{0}{1}'.format(self.output_directory_name, self.output_file_name)

        write_mode = self._get_write_mode(output_file_path)

        fieldnames = ['related_article_doi', 'url', 'source', 'date_posted']

        try:

            with open(output_file_path, write_mode) as output_csv:

                output_writer = DictWriter(output_csv, fieldnames=fieldnames)

                if write_mode == 'w':
                    output_writer.writeheader()

                for mention in self.mentions_list:

                    output_dict = dict(related_article_doi=mention.related_article_doi,
                                       url=mention.url,
                                       source=mention.source,
                                       date_posted=mention.date_posted)

                    output_writer.writerow(output_dict)

        except:

            print('Something totally unexpected happened when trying to write to a Master CSV file')
            print('The writer was setup to write to a file called {0}{1}'.format(self.output_directory_name,
                                                                                 self.output_file_name))
            if write_mode == 'a':
                print('The writer thought this file existed and was trying to append to it.')
            elif write_mode == 'w':

                print('The writer thought this was a brand new file and was trying to create it.')
            else:
                print('The writer could not determine whether or not the file existed.')
