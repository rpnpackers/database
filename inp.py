# input

# Call this function with the question that you want to ask. 
def get_int(s, min=None, max=None):
    while True:
        # Saves the input under t using the given string
        t = input(s)
        r = False
        # Checks to see if a range was given.
        if max != None and min != None:
            r = True
        
        # Exits the throw an error if it isn't an integer. 
        if not t.isnumeric():
            print("Input must be entirely numerical")
            
        else:
            x = int(t) 
            if r and (x >= min and x <= max) or not r:
                return int(t)
            elif r:
                print(f"Must be between {min} and {max} inclusive.")

def user_choice(options, text=None):
    # Check for correct input
    # Takes as input a list of letter options, and their corresponding meanings.
    choice = None
    # Handles where shorter output is better
    if text == None:
         while choice not in options:
            # Gets the input
            choice = input("Choose a function: ").lower()
         return choice[0]

    if (len(options) != len(text)):
        raise IOError
    while choice not in options:
        print("Options:")
        for i in range(len(options)):
            print(f"{text[i]} = {options[i]}")
        # Gets the input
        choice = input("Choose a function: ").lower()
    return choice[0]
