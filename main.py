import classes
import data
import sys


def main():

    # Open operations file
    try:
        file = open(sys.argv[1])
    except:
        print("ERROR - Cannot open operation file")

    # Count data entries
    count = 0
    for Transaction in data.main_data:
        count = count + 1
    print(count, "transactions loaded")

    # Totals for each category
    for Transaction in data.main_data:
        if Transaction.category in data.totals:
            data.totals[Transaction.category] = data.totals[Transaction.category] + Transaction.dollar
        else:
            data.totals["Not Listed"] = data.totals["Not Listed"] + Transaction.dollar
    print(data.totals)






test = main()