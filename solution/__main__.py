import os
import sys

from heuristics import heuristic
from parser import parse
from submission import SubmissionMaker


if __name__ == '__main__':
    for file_path in sys.argv[1:]:
        print(file_path)
        data_file_path = file_path
        results = parse(data_file_path)
        submission_maker = SubmissionMaker(os.path.basename(file_path))
        current_days = 0
        while len(results.libraries) > 0 and current_days < results.days:
            library = heuristic().getNextLib(results.libraries)
            results.libraries.remove(library)
            submission_maker.addLibrary(library)
            current_days += library.signup_days
            lifetime_nbooks = (results.days - current_days) * library.scan_rate 
            for book in library.books[:lifetime_nbooks]:
                book.banned = True
        submission_maker.makeSubmission()
