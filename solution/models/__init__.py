class Library():
    def __init__(self, id_, signup_days, scan_rate):
        self.id = id_
        self.signup_days = signup_days
        self.scan_rate = scan_rate
        self.books = []

    def __str__(self):
        return str(self.id)


class Book():
    def __init__(self, id_, score):
        self.id = id_
        self.score = score
        self.banned = False
