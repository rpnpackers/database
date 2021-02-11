import csv
import sys
import sqlite3

# Checks for correct command line arguments
if len(sys.argv) != 2:
    print("Usage: data1.py input.csv")
    exit(1)

# Get input about the Column titles
print("Omit all spaces from the endss!!!")
name = input("Title of Name Column: ")
info = input("Title of Data column: ")
kw = input("kWh = 1, Wh = 0: ")
num = int(input("Number of the month (eg: Sept == 9): "))
y = input("Year: ")

# Change the year into it's table equivalent
table = "y" + str(y)

# Opens the csv File as data
t = open(sys.argv[1], 'r')
data = csv.DictReader(t)

# Establish connection to database
conn = sqlite3.connect('monthlyusage.db')
c = conn.cursor()

# Creates the Strings for the database
db = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
dbm = num - 1    # Creates a variable for finding the correct month

# Creates a list of the projects that were added
new_projects = []

# Iterates through each row of the Montly data
for row in data:
    # Check to see if the project is in the database, and add it if it's not
    c.execute("SELECT COUNT(*) FROM projects WHERE name==?;", [row[name]])
    temp = c.fetchall()
    y = [z[0] for z in temp]
    repeat = y[0]
    if repeat == 0:
        c.execute("INSERT INTO projects (name) VALUES(?);", [row[name]])
        new_projects.append(row[name])
    
     # Gets the tid
        c.execute("SELECT tid FROM projects WHERE name ==?", [row[name]])
        temp = c.fetchall()
        y = [z[0] for z in temp]
        tid = y[0]

        # Add data to the sql
        # Have to check for rows that exist already (repeat holds the number of rows with the tid)
        c.execute("SELECT COUNT(*) FROM " + table + " WHERE tid==?;", [tid])
        temp = c.fetchall()
        y = [z[0] for z in temp]
        repeat = y[0]

        # Accounts for Wh and kWh 
        if kw != 1:
            z = int(row[info]) / 1000
        else: 
            z = int(row[info])

        # If this project already has a row in this year
        if repeat != 0:
            c.execute("UPDATE " + table + " SET " + db[dbm] + "=? WHERE tid ==?;", (z, tid))
        # Creates a new row 
        else:
            c.execute("INSERT INTO " + table + " (tid, " + db[dbm] + ") VALUES(?,?);", (tid, z))

# Handles additional data
if bool(new_projects):
    print("These projects were added while adding to the database:")
    for i in range(len(new_projects)):
        print(new_projects[i])
t.close()
conn.commit()
conn.close()