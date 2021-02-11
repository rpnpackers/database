import csv
import sqlite3
import sys

# Checks for correct command line arguments
if len(sys.argv) != 2:
    print("Usage: data1.py input.csv")
    exit(1)

# Get data about the information to be inported
month = int(input("Starting month number (eg: september = 9): "))       # Number of the first month
count = int(input("Number of months to be imported (Can't go past end of year): ")) # Number of Months 
year = int(input("Year of the imported data: "))                        # Number for the original year
table = "y" + str(year)                                                 # The name of the table that will be changed

# handles extra months
if month + count - 1 > 12:
    count = 12 - month + 1

# Creates the Strings for the database
db = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
dbm = month - 1    # Creates a variable for finding the correct month

# Creates the strings for months to read from the original csv
columns = []
for i in range(count):
    columns.append(str(month + i) + "/1/" + str(year))

# Establish connection to database
conn = sqlite3.connect('monthlyusage.db')
c = conn.cursor()

# For loop to iterate through each column
for i in range(count):
    # Opens the Csv
    t = open(sys.argv[1], 'r')
    names = csv.DictReader(t)

    for row in names:
        # Gets the tid
        name = row['Name']
        c.execute("SELECT tid FROM projects WHERE name ==?", [name])
        temp = c.fetchall()
        y = [z[0] for z in temp]
        tid = y[0]

        # Add data to the sql
        # Have to check for rows that exist already (repeat holds the number of rows with the tid)
        c.execute("SELECT COUNT(*) FROM " + table + " WHERE tid==?;", [tid])
        temp = c.fetchall()
        y = [z[0] for z in temp]
        repeat = y[0]

        # If this project already has a row in this year
        if repeat != 0:
            c.execute("UPDATE " + table + " SET " + db[dbm] + "=? WHERE tid ==?;", (row[columns[i]], tid))
        # Creates a new row 
        else:
            c.execute("INSERT INTO " + table + " (tid, " + db[dbm] + ") VALUES(?,?);", (tid, row[columns[i]]))

    # Closes the csv
    t.close()
    dbm += 1

conn.commit()