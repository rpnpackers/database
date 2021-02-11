import csv 
import sqlite3

# Gets the file name from the user
while True:
    a = input("Csv File Path: ")
    try: 
        t = open(a, 'r')
    except IOError:
        print("File not found, type exact path.\nExample: import_files\\file.csv")
    else:
        break
# Read the csv into a dictionary
names = csv.DictReader(t)

# Establish a connection to the database
while True:
    a = input("Database File Path: ")
    if 
c = conn.cursor()