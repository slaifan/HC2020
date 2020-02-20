from models import *


def parse(data_file_path):
    with open(data_file_path) as data_file:
        libraries = []
        for i, line in enumerate(data_file):
            if i == 0:
                _, __, days = line.split()
            elif i == 1:
                books = [Book(book_id, score) for book_id, score in enumerate(line.split())]
            elif i % 2 == 0:
                _, signup_days, scan_rate = line.split()
                libraries.append(Library(signup_days, scan_rate))
            else:
                libraries[len(libraries) - 1].books = [books(book_id) for book_id in line.split()]
    return ParseResults(books, libraries, days)

class ParseResults():
    def __init__(self, books, libraries, days):
        self.books = books
        self.libraries = libraries
        self.days = days
