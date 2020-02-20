# from models import *

class heuristic:
    def __init__(self):
        self.usedBooks = set({})
        self.day = 0
    def heuristicCal(self,lib, UsedBooks):
        score = 0
        for book in lib.books:
            score+= book.score
            score = score/len(lib.books)
        temp = lib.signup_days + (len(lib.books)/lib.scan_rate)
        return score/temp
    def findMaxLib(self,libs):
        bestScore = 0
        bestLib = None
        for lib in libs:
            score = self.heuristicCal(lib))
            if(bestScore < score):
                bestScore = score
                bestLib = lib
    def getNextLib(self,libs):
        return self.findMaxLib(libs)
