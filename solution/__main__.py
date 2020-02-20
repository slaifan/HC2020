import sys

from parser import parse


if __name__ == '__main__':
    data_file_path = sys.argv[1]
    results = parse(data_file_path)
    print(f'There are {len(results.libraries)} libraries, {len(results.books)} books, and {results.days} days')
    book_scores = [book.score for book in results.books]
    print(f'The scores of the books are {book_scores}')
    for library in results.libraries:
        print(f'Library {library.id} has {len(library.books)} books, the signup process takes {library.signup_days} days, and the library can ship {library.scan_rate} books per day.')
        book_ids = [book.id for book in library.books]
        print(f'The books in library {library.id} are: {book_ids}')
