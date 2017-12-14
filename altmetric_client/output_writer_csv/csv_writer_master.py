from altmetric_client.output_writer_csv.csv_writer_base import CSVWriterBase
from altmetric_client.altmetric import Altmetric
from csv import DictWriter
import os.path


class CSVWriterMaster(CSVWriterBase):

    def __init__(self,
                 output_file_name=None,
                 output_directory_name=None,
                 altmetric=None):

        CSVWriterBase.__init__(self, output_file_name, output_directory_name)
        self._altmetric = altmetric

    @property
    def altmetric(self):
        return self._altmetric

    @altmetric.setter
    def altmetric(self, altmetric: Altmetric):
        self._altmetric = altmetric

    def write_master(self):

        output_file_path = '{0}{1}'.format(self.output_directory_name, self.output_file_name)

        if not self._setup_is_valid():
            return

        write_mode = self._get_write_mode(output_file_path)

        fieldnames = ['doi', 'altmetric_id', 'altmetric_score', 'type', 'article_title',
                      'journal_title', 'journal_volume', 'journal_issue', 'page_starts', 'page_ends',
                      'publisher', 'altmetric_journal_id', 'total_mentions',
                      'print_publication_date','first_seen_on_date', 'last_mentioned_date',
                      'first_author', 'pdf_url', 'uri', 'mendeley_url']

        try:

            with open(output_file_path, write_mode) as output_csv:

                output_writer = DictWriter(output_csv, fieldnames=fieldnames)

                if write_mode == 'w':
                    output_writer.writeheader()

                output_dict = dict(doi=self.altmetric.doi,
                                   altmetric_id=self.altmetric.altmetric_id,
                                   altmetric_score=self.altmetric.altmetric_score,
                                   type=self.altmetric.type,
                                   article_title=self.altmetric.article_title,
                                   journal_title=self.altmetric.journal_title,
                                   journal_volume=self.altmetric.journal_volume,
                                   journal_issue=self.altmetric.journal_issue,
                                   page_starts=self.altmetric.page_starts,
                                   page_ends=self.altmetric.page_ends,
                                   publisher=self.altmetric.publisher,
                                   altmetric_journal_id=self.altmetric.altmetric_journal_id,
                                   total_mentions=self.altmetric.total_mentions,
                                   print_publication_date=self.altmetric.print_publication_date,
                                   first_seen_on_date=self.altmetric.first_seen_on_date,
                                   last_mentioned_date=self.altmetric.last_mentioned_date,
                                   first_author=self.altmetric.first_author,
                                   pdf_url=self.altmetric.pdf_url,
                                   uri=self.altmetric.uri,
                                   mendeley_url=self.altmetric.mendeley_url)

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

    def _setup_is_valid(self):

        if self.output_file_name is None:

            print('Could not write a master csv file because the filename was not set in the Master CSV Writer')
            return False

        elif self.output_directory_name is None:

            print('Could not write a master csv file because the output directory was not set in the Master CSV Writer')
            return False

        elif self.altmetric is None:

            print('Could not write a master csv file because the Altmetric data was not set in the Master CSV Writer')
            return False

        else:

            return True

