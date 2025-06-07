CSC 101 - Final Project - Ethan Gallagher & Nathan Lee

class.py -> has all classes used, including Transaction and Date
data.py -> has all data used, including list of transactions and dictionaries
driver.py -> the python program to run
main.py -> main python code containing various functions
operations.txt -> text files with operations to filter data

** OPERATION COMMANDS **
Each command should be in a new line.

Budget Categories: "Donation", "Entertainment", "Food",
"Grocery","Supplies","Shopping","Sports","Travel","Misc","Not Listed

Adding a budget:
set_budget:CATEGORY:VALUE

Adding a transaction:
add_transaction:Month(MM).DD.YYYY:value:category:name

View Monthly:
month:Month(MM):Category

Compare to budget:
compare:Month(MM):Category

Reset budget and transactions:
reset