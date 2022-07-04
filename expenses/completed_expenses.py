# Gets expenses, returns a list which has..
# Gets expenses, returns a list which has..
# The data-frame and sub-total...
def get_expenses(var_fixed):

    # Setup dictionaries

    item_list = []
    quantity_list = []
    price_list = []

    variable_dict = {
        "Item": item_list,
        "Quantity": quantity_list,
        "Price": price_list
    }

    # Loop to get component, quantity and price
    item_name = ""
    while item_name.lower() != "xxx":

        print()
        # Get name, quantity and item
        item_name = not_blank("Item name: ", "The component name can't be blank.")
        print("The item you have chosen is: ", item_name)
        print()

        if item_name.lower() == "xxx":
            break
    
        quantity = num_check("Quantity", "The component name cannot be blank", int)
        
        price = num_check("How much? $", "The price must be a number more than zero", float)

        # Add item, quantity and price to lists
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

    expense_frame = pandas.DataFrame(variable_dict)
    expense_frame = expense_frame.set_index('Item')

    # Calculate the cost of each component
    expense_frame['Cost'] = expense_frame['Quantity'] * expense_frame['Price']

    # Find sub total..
    sub_total = expense_frame['Cost'].sum()

    # Currency Formatting (uses currency function)
    add_dollars = ['Price', 'Cost']
    for item in add_dollars:
        expense_frame[item] = expense_frame[item].apply(currency)

    return [expense_frame, sub_total]
