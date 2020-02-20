class SubmissionMaker():
   def __init__(self):
      self.libraryCount = 0
      self.libraries = {}     ## format: {id : len books}
      self.books = set()

   def addLibrary(self, library): ## when scanning a library
      self.libraryCount++
      self.libraries[library] = len(library.books)
   
   def getBooks(self, library) ## not ordered
      for book in library.books:
         self.books.add(book)
   
   def makeSubmission(self): ## still need to write added books
      submission = open("submission.txt","a")
      submission.write(self.libraryCount)
      for library in self.libraries.keys():
         submission.write(library + " " + libraries.get(library))
<<<<<<< HEAD
         bookcol = ""
         for book in self.getBooks(library):
            bookcol += book.id + " "
         submission.write(bookcol)
         submission.close()
=======
         ## sort library books and write here
>>>>>>> 677cba6774c3e1cd6c90a9d902d84e6f1f35fb7b
