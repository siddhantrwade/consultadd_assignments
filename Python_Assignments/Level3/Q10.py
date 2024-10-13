def user_checker(n, customers):

    occupied_computers = set()
    unavailable = 0

    for customer in customers:

        if customer in occupied_computers: # if cust tries a comp in use

            occupied_computers.remove(customer)
        elif len(occupied_computers) < n: # computers available
            occupied_computers.add(customer)
        else:
            unavailable += 1 # put customer in queue

    return unavailable

n = 5 # available computers
customer_order = "AABCDEEFDDGHFJKJJDK"

waiting = user_checker(n, customer_order)

print('Customers still waiting to get in', waiting)