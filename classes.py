class Transaction:

    def __init__(self, Date, dollar, category, name):
        self.date = Date
        self.dollar = dollar
        self.category = category
        self.name = name

    def __repr__(self):
        return "Transaction({}, {}, {}, {})".format(self.date, self.dollar, self.category, self.name)

    def __eq__(self, other):
        return (self is other or
                type(other) == type(Transaction) and
                self.date == other.date and
                self.dollar == other.dollar and
                self.category == other.category and
                self.name == other.name)


class Date:

    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year

    def __repr__(self):
        return "Date({}, {}, {})".format(self.month, self.day, self.year)

    def __eq__(self, other):
        return (self is other or
                type(other) == type(Date) and
                self.month == other.month and
                self.day == other.day and
                self.year == other.year)
