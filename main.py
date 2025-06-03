import sys
import data
import classes
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
                print("Over monthly budget of ${} by ${}".format(data.monthly[broken[2]], round(month_total - data.monthly[broken[2]], 2)))
            elif month_total == data.monthly[broken[2]]:
                print("Equal to budget (${})".format(data.monthly[broken[2]]))
            else:
                print("Under monthly budget of ${} by ${}".format(data.monthly[broken[2]], round(data.monthly[broken[2]] - month_total, 2)))

        # Resets the transaction log and budgets
        elif command == "reset":
            reset()
            for i in range(len(data.main_data)):
                del data.main_data[0]

        elif command == "add_transaction":
            date_list = broken[1].split(".")
            month = ''.join([char for char in date_list[0] if char.isdigit()])
            day = date_list[1]
            year = date_list[2]
            value = broken[2]
            category = broken[3]
            name = broken[4]
            new_transaction = classes.Transaction(Date(month, day, year), value, category, name)
            data.main_data.append(new_transaction)
            print("The Transaction " + "{}".format(str(new_transaction)) + " has been recorded.")

        # Skipping blank lines
        elif command == "":
            continue

        # Error message
        else:
            print("ERROR - Malfunctioned operation on line {}".format(op_count))


# This function resets the expense and count total dictionaries back to 0
def reset():

    # Resetting expense and count totals
    for cat in data.totals:
        data.totals[cat] = 0
        data.counts[cat] = 0
