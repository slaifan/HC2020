# from models import *

class heuristic:
    def __init__(self):
        self.usedBooks = set({})
        self.day = 0

    def heuristicCal(self,lib):
        score = 0
        books = []
        for book in lib.books:
            if not book.banned:
                books.append(book)
        for book in books:
            score += book.score
            score = score/len(books)
        temp = lib.signup_days + (len(books)/lib.scan_rate)
        return score/temp

    def findMaxLib(self,libs):
        bestScore = 0
        bestLib = None
        for lib in libs:
            score = self.heuristicCal(lib)
            if(bestScore < score):
                bestScore = score
                bestLib = lib
        return bestLib

    def getNextLib(self,libs):
        return self.findMaxLib(libs)
