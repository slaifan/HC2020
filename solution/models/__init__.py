class Library():
    def __init__(self, id_, signup_days, scan_rate):
        self.id_ = id_
        self.signup_days = signup_days
        self.scan_rate = scan_rate
        self.books = []


class Book():
    def __init__(self, id_, score):
        self.id_ = id_
        self.score = score
