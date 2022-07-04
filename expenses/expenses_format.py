# Prints expenses frame..
def expense_print(heading, frame, subtotal):
    print()
    print("** {} Costs **".format(heading))
    print(frame)
    print()
    print("{} Costs: ${:.2f}".format(heading, subtotal))
    return ""
