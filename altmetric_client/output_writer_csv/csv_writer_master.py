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

        write_mode = self._get_write_mode(output_file_path)

        fieldnames = ['altmetric_id', 'altmetric_score', 'article_title', 'journal_title', 'altmetric_journal_id',
                      'total_mentions', 'print_publication_date', 'first_seen_on_date', 'authors']

        with open(output_file_path, write_mode) as output_csv:

            output_writer = DictWriter(output_csv, fieldnames=fieldnames)

            if write_mode == 'w':
                output_writer.writeheader()

            output_dict = dict(altmetric_id=self.altmetric.altmetric_id,
                               altmetric_score=self.altmetric.altmetric_score,
                               article_title=self.altmetric.article_title,
                               journal_title=self.altmetric.journal_title,
                               altmetric_journal_id=self.altmetric.altmetric_journal_id,
                               total_mentions=self.altmetric.total_mentions,
                               print_publication_date=self.altmetric.print_publication_date,
                               first_seen_on_date=self.altmetric.first_seen_on_date,
                               authors=self.altmetric.authors)

            output_writer.writerow(output_dict)

    def _get_write_mode(self, filepath):

        if os.path.isfile(filepath):
            return 'a'
        else:
            return 'w'
