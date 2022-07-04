# Checks that user has entered either 'yes' or 'no'...
def yes_no(question):

    to_check = ["yes", "no"]

    valid = False
    while not valid:

        response = input(question).lower()

        for var_item in to_check:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return response

        print("Please enter either yes or no...\n")

# Checks that user has not completed anything with blank errors
def not_blank(question, error):

    valid = False
    while not valid:
        response = input(question)
    
        if response == "":
            print("{}. \nPlease try again.\n".format(error))
            continue

        return response
