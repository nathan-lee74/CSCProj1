# Representation of a transaction
class Transaction:

    # Initialize a new Transaction object
    # input: the transaction date
    # input: the dollar amount of transaction
    # input: the category of transaction
    # input: the origin of transaction
    def __init__(self, Date, dollar, category, name):
        self.date = Date
        self.dollar = dollar
        self.category = category
        self.name = name

    # Provide a developer-friendly string representation of object
    # input: Transaction for which the string is desired
    # output: string representation

    # string representation for transaction.
    def __str__(self):
        return "Name: {}, Value: {}, Date: {}, Category: {}".format(self.name, self.dollar, self.date, self.category)

    def __repr__(self):
        return "Transaction({}, {}, {}, {})".format(self.date, self.dollar, self.category, self.name)

    # Compare the transaction with another object for equality
    # input: Transaction to compare
    # input: another value to compare with
    # output: boolean indicating equality
    def __eq__(self, other):
        return (self is other or
                type(other) == type(Transaction) and
                self.date == other.date and
                self.dollar == other.dollar and
                self.category == other.category and
                self.name == other.name)


# Representation of Date
class Date:

    # Initialize a new Date object
    # input: the date month
    # input: the date day
    # input: the date year
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year

    # Provide a developer-friendly string representation of object
    # input: Date for which the string is desired
    # output: string representation
    def __repr__(self):
        return "Date({}, {}, {})".format(self.month, self.day, self.year)

    # Compare the date with another object for equality
    # input: Date to compare
    # input: another value to compare with
    # output: boolean indicating equality
    def __eq__(self, other):
        return (self is other or
                type(other) == type(Date) and
                self.month == other.month and
                self.day == other.day and
                self.year == other.year)
