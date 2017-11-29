from altmetric_client.altmetric import Altmetric
from altmetric_client.output_writer_csv.csv_writer_master import CSVWriterMaster
from altmetric_client.output_writer_csv.csv_writer_mentions import CSVWriterMention
from altmetric_client.output_writer_csv.csv_writer_author import CSVWriterAuthor

class CSVWriterFacade:

    def __init__(self, output_directory_name, output_files_root):

        self.__output_directory_name = output_directory_name
        self.__output_files_root = output_files_root

        self.__csv_master_writer = CSVWriterMaster('{0}_master.csv'.format(output_files_root), output_directory_name)
        self.__csv_mentions_writer = CSVWriterMention('{0}_mentions.csv'.format(output_files_root), output_directory_name)
        self.__csv_authors_writer = CSVWriterAuthor('{0}_authors.csv'.format(output_files_root), output_directory_name)

    @property
    def output_directory_name(self):
        return self.__output_directory_name

    @output_directory_name.setter
    def output_directory_name(self, output_directory_name):
        self.__output_directory_name = output_directory_name

    @property
    def output_files_root(self):
        return self.__output_files_root

    @output_files_root.setter
    def output_files_root(self, output_files_root):
        self.__output_files_root = output_files_root

    def write(self, altmetric:Altmetric):

        self.__csv_master_writer.altmetric = altmetric
        self.__csv_master_writer.write_master()

        self.__csv_mentions_writer.mentions_list = altmetric.mentions
        self.__csv_mentions_writer.write_mentions()

        print('{0} mentions successfully written for altmetric with DOI {1}'.format(len(altmetric.mentions),
                                                                                    altmetric.doi))

    def write_authors(self, authors_list):

        self.__csv_authors_writer.authors_list = authors_list
        self.__csv_authors_writer.write_authors()

        print('{0} authors successfully written'.format(len(authors_list)))
