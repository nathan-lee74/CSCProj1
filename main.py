import sys
import data
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

    # Total expenses per category (rounded to 2 decimal places) and total counts per category
    for Transaction in data:
        if Transaction.category in expense:
            expense[Transaction.category] = expense[Transaction.category] + Transaction.dollar
            counts[Transaction.category] = counts[Transaction.category] + 1
        else:
            expense["Not Listed"] = expense["Not Listed"] + Transaction.dollar
            counts["Not Listed"] = counts["Not Listed"] + 1
    for Cat in expense:
        expense[Cat] = round(expense[Cat], 2)


# This function goes through every operation listed in the operations.txt file
def operations():

    # Open operations file
    try:
        file = open(sys.argv[1])
    except:
        print("ERROR - Cannot open operation file")

    # Operations
    op_count = 0
    for line in file:
        broken = line.strip("\n").split(":")
        command = broken[0]
        op_count = op_count + 1

        # Grabbing specific monthly information
        if command == "month":
            month_total = 0
            month_count = 0
            for Transaction in data.main_data:
                if str(Transaction.date.month) in broken[1] and broken[2] == Transaction.category:
                    month_total = round(month_total + Transaction.dollar, 2)
                    month_count = month_count + 1
            print("{} {} information: expense = ${}, count = {}".format(broken[1],broken[2],month_total,month_count))

        # Comparing to monthly budget
        elif command == "compare":
            month_total = 0
            for Transaction in data.main_data:
                if str(Transaction.date.month) in broken[1] and broken[2] == Transaction.category:
                    month_total = round(month_total + Transaction.dollar, 2)
            if month_total > data.monthly[broken[2]]:
                print("Over budget by ${}".format(round(month_total - data.monthly[broken[2]], 2)))
            elif month_total == data.monthly[broken[2]]:
                print("Equal to budget (${})".format(data.monthly[broken[2]]))
            else:
                print("Under budget by ${}".format(round(data.monthly[broken[2]] - month_total, 2)))

        # Skipping blank lines
        elif command == "":
            continue

        # Error message
        else:
            print("ERROR - Malfunctioned operation on line {}".format(op_count))
