import csv 
import sqlite3
import sys 
import inp
import db

def main():
    # While loop so that multiple operations can be performed.
    while True:
        # Gets input from the user about what they want to do 
        options = ["j", "m", "o", "q"]
        text = ["Import Jobs", "Import Montly Data", "Import Original Data", "Quit"]
        choice = inp.user_choice(options, text)
        
        # Runs the specific methods for each operation
        if choice == "j":
            jobs()
        elif choice == "m":
            monthly()
        elif choice == "o":
            original()
        elif choice == "q":
            break
        else:
            print ("Input error, review code")
            break 
        


# Method for importing jobs
def jobs():
    import os

    # Gets the file name from the user
    while True:
        a = input("Csv File Path: ")
        try: 
            t = open(a, 'r')
        except IOError:
            print("File not found, type exact path.\nExample: import_files\\file.csv")
        else:
            break

    # Establish a connection to the database
    while True:
        a = input("Database File Path: ")
        # Check that the file exists
        if os.path.isfile(a):
            break
        else:
            print("File must exist, check spelling")
    conn = sqlite3.connect(a)
    c = conn.cursor()

    
    # Read the csv into a dictionary
    names = csv.DictReader(t)
    # Get names of the column titles
    print("Input the title names from the csv file.\nBe sure to omit all spaces")
    titles = db.column_name(2, names)
    # Iterate through each row of the system. 
    for row in names:
        # Search the Database for jobs with the samvae first word or id 
        x = [row[titles[0]], row[titles[1]]]
        exist = db.check_similar(x, a)
        
        # prompt user to change 
        if exist != None:
            print("Are these two projects the same?")
            print(f"Database:\n{exist}")
            print(f"CSV:\n{row[titles[0]]} {row[titles[1]]}")

            # Ask user to verify if they're the same project
            

        
        
# Method for importing monthly data
def monthly():
    print("Added monthly data!!!\n\n")

# Method for importing data from the original file
def original():
    print("Added data from original!!!\n\n")

jobs()