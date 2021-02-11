import csv
import sqlite3
import sys

# Checks for correct command line arguments
if len(sys.argv) != 2:
    print("Usage: originalimport.py input.csv")
    exit(1)

# Opens the Csv
t = open(sys.argv[1], 'r')
names = csv.DictReader(t)

# Establish connection to database
conn = sqlite3.connect('monthlyusage.db')
c = conn.cursor()

# Iterates through each row to add each system
for row in names:
    # Imports the Data
    if row['ID'] == '':
        c.execute("INSERT INTO projects (name) VALUES(?)", [row['Name']])
    else:
        c.execute("INSERT INTO projects (id, name) VALUES(?,?)", [int(row['ID']), row['Name']])
conn.commit()
conn.close()
t.close()