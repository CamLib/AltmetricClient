from altmetric_client.altmetric import Altmetric
from csv import DictWriter
import os.path


class CSVWriterMaster:
    def __init__(self,
                 output_file_name=None,
                 output_directory_name=None,
                 altmetric=None):
        self._output_file_name = output_file_name
        self._output_directory_name = output_directory_name
        self._altmetric = altmetric

    @property
    def output_file_name(self):
        return self._output_file_name

    @output_file_name.setter
    def output_file_name(self, output_file_name):
        self._output_file_name = output_file_name

    @property
    def output_directory_name(self):
        return self._output_directory_name

    @output_directory_name.setter
    def output_directory_name(self, output_directory_name):
        self._output_directory_name = output_directory_name

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

        fieldnames = ['doi', 'altmetric_id', 'altmetric_score', 'article_title', 'journal_title',
                      'altmetric_journal_id','total_mentions', 'print_publication_date', 'first_seen_on_date',
                      'authors']

        try:

            with open(output_file_path, write_mode) as output_csv:

                output_writer = DictWriter(output_csv, fieldnames=fieldnames)

                if write_mode == 'w':
                    output_writer.writeheader()

                output_dict = dict(doi=self.altmetric.doi,
                                   altmetric_id=self.altmetric.altmetric_id,
                                   altmetric_score=self.altmetric.altmetric_score,
                                   article_title=self.altmetric.article_title,
                                   journal_title=self.altmetric.journal_title,
                                   altmetric_journal_id=self.altmetric.altmetric_journal_id,
                                   total_mentions=self.altmetric.total_mentions,
                                   print_publication_date=self.altmetric.print_publication_date,
                                   first_seen_on_date=self.altmetric.first_seen_on_date,
                                   authors=self.altmetric.first_author)

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

    def _get_write_mode(self, filepath):

        if os.path.isfile(filepath):
            return 'a'
        else:
            return 'w'
