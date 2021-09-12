from abc import ABC, abstractmethod


class FileReader(ABC):

    def operate(self):
        self.open_file()
        self.extract_file_content()
        self.extract_file_content()
        self.do_something()
        self.close_file()

    def open_file(self):
        print('File open')

    def do_something(self):
        print('do something')

    def close_file(self):
        print('File close')

    @abstractmethod
    def extract_file_content(self):
        pass

    @abstractmethod
    def parse_file_content(self):
        pass


class CSVFileReader(FileReader):

    def extract_file_content(self):
        print('CSV File extract content')

    def parse_file_content(self):
        print('CSV File parse content')


class ExcelFileReader(FileReader):

    def extract_file_content(self):
        print('Excel File extract content')

    def parse_file_content(self):
        print('Excel File parse content')


"""
File open
CSV File extract content
CSV File extract content
do something
File close

File open
Excel File extract content
Excel File extract content
do something
File close
"""


def client_code():
    csv_reader = CSVFileReader()
    csv_reader.operate()

    excel_reader = ExcelFileReader()
    excel_reader.operate()


client_code()
