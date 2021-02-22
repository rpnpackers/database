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
    print ("Use ID column then Name column.")
    titles = db.column_name(2, names)
    # Iterate through each row of the system. 
    for row in names:
        # Search the Database for jobs with the samvae first word or id 
        x = [row[titles[0]], row[titles[1]]]
        database = db.check_similar(x, a)
        
        # prompt user to change 
        if database != None:
            print("Are these two projects the same?")
            print(f"Database: {database}")
            print(f"CSV:         {row[titles[1]]} {row[titles[0]]}")

            # Ask user to verify if they're the same project
            options = ["y", "n"]
            print("Yes for the same, and No for different")
            if inp.user_choice(options) == "y":
                # if yes, offer to modify entry
                if inp.user_choice(["d", "c"], ["Database", "Csv"]) == "d":
                    continue
                else:
                    # Change Name in Database usint tid databases[0][2]
                    c.execute("""UPDATE projects
                                SET name = ?, id = ? WHERE tid ==?;""", (row[titles[1]], row[titles[0]], database[2]))
            else:
                c.execute("INSERT INTO projects (name, id) VALUES (?, ?);", (row[titles[1]], row[titles[0]]))
    # Save and close 
    t.close()
    conn.commit()
    conn.close()




# Method for importing monthly data
def monthly():
    # Get input from the user
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

    # Get Column Names
    print("Use ID then Name")
    titles = db.column_name(2)
    # Specific input
    kw = inp.user_choice([1, 0], ["kWh", "Wh"])
    print("Input the number of the month: ")
    num = db.user_choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    year = input("Input the year: ")
    
    # Change the year into it's table equvalent
    table = "y" + str(year)

    # Opens the CSV file 
    t = open(sys.argv[1], 'r')
    data = csv.DictReader(t)

    # Creates the Strings for the database
    db = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
    dbm = num - 1    # Creates a variable for finding the correct month

    for row in data: 
        # check if they have similar name (tid must be different)

# Method for importing data from the original file
def original():
    print("Added data from original!!!\n\n")

jobs()