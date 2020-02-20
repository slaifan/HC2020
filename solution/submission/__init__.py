class SubmissionMaker():
    def __init__(self, filename):
        self.filename = filename
        self.libraryCount = 0
        self.libraries = {}     ## format: {id : len books}
        self.books = set()

    def addLibrary(self, library): ## when scanning a library
        self.libraryCount += 1
        self.libraries[library] = len(library.books)

    def getBooks(self, library): ## not ordered
        for book in library.books:
            self.books.add(book)

    def makeSubmission(self): ## still need to write added books
        with open(self.filename,"w") as submission:
            submission.write(f'{str(self.libraryCount)}\n')
            for library in self.libraries.keys():
                submission.write(f'{library} {self.libraries.get(library)}\n')
                bookcol = []
                for book in library.books:
                    bookcol.append(book.id)
                bookcol = ' '.join([str(id_) for id_ in bookcol])
                submission.write(f'{str(bookcol)}\n')
