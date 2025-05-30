import sys
from classes import *

# This main function sums the total expense and count for each category given
# input: list of transactions acting as the data set
# input: a dictionary to represent the total expense for each category
# input: a dictionary to represent the total count for each category
# output: updated dictionary of total expenses per category
# output: updated dictionary of total counts per category
def sums(data:list[Transaction], expense:dict, counts:dict):

    # Count data entries
    count = 0
    for Transaction in data:
        count = count + 1
    print(count, "transactions loaded")

    # Total expense and counts for each category
    for Transaction in data:
        if Transaction.category in expense:
            expense[Transaction.category] = expense[Transaction.category] + Transaction.dollar
            counts[Transaction.category] = counts[Transaction.category] + 1
        else:
            expense["Not Listed"] = expense["Not Listed"] + Transaction.dollar
            counts["Not Listed"] = counts["Not Listed"] + 1


def operations():

    # Open operations file
    try:
        file = open(sys.argv[1])
    except:
        print("ERROR - Cannot open operation file")
