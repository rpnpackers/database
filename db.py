# db.py>

# Get input for column headers
# input the number of columns
def column_name(num_of_titles, in_csv):
    headers = []
    for i in range(num_of_titles):
        t = input(f"Title {i + 1}:")
        headers.append(t)
    return headers

# Checks for similar project entries
# name_id is a list with the name in 0 and id in 2
def check_similar(name_id, database):
    import sqlite3
    # Establishes Connection
    conn = sqlite3.connect(database)
    c = conn.cursor()
    # Select with same id
    c.execute("SELECT name, id, tid FROM projects WHERE projects.id == ?;", [name_id[0]])
    temp = c.fetchone()
    # Exit if the project exists, and return it's info 
    if temp != None:
        # Check to ensure they aren't exact, if so return none.
        return temp
    # If the id isn't in the database, then check the first and last word of name
    else:
        temp = name_id[1].split()
        if len(temp) > 1:
            c.execute(f"""SELECT name, id, tid FROM projects WHERE name 
                        LIKE '{temp[0]}%{temp[len(temp) - 1]}';""")
        else:
            c.execute(f"""SELECT name, id, tid FROM projects WHERE name
                        LIKE '{temp[0]}';""")
        x = c.fetchone()
        if x != None:
            return x