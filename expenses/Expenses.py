

def num_check(question, error, num_type):...



def not_blank(question, error):

    valid = False
    while not valid:
        response = input (question)


        if response == "":
            print("{}.  \nPlease try again.\n".format(error))
            continue


        return response



#  ****** Main routine starts her ******

# set up dictionaries and lists

items_lists = []
quantity_list = []
price_list = []

variable_dict = {
    "item": item_list,
    "quantity": quantity_list,
    "price": price_list
}


# Get user data
product_name = not_blank("product name: ", "the product name can't be blank.")

# loop to get component, quantity and price
item_name= ""
while item_name.lower() != "xxx":

    print()
    # get name, quantity and item
    item_name = not_blank("item name: ", "the component name can't be Blank")


    if item_name.lower() == "xxx":
        break

    quantity = num_check("quantity:","the amount must be a whole number more then zero",int)

    price = num_check("How much for a single item? $","the price must be a number <more than 0>".Float)


    # add item, quantity and price to lists
    item_list.append(item_name)
    quantity_list.append(quantity)
    price_list.append(price)


variable_frame = panda.dataframe(variable_dirt)
variable_frame = variable_frame.set_index('Item')

# calculate cost of each component
variable_sub = variable_frame['cost'].sum()

# currency formatting (uses currency funtion)
add_dollars = ['price', 'cost']
for item in add_dollars:
    variable_frame[item] = variable_frame[item].apply(currency))

# *** Printing Area ***

print (variable_frame)