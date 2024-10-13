def measures(lst):

    print('Mean temperature is:', sum(lst) / len(lst))
    print('Max temperature is:', max(lst))
    print('Min temperature is:', min(lst))

# Accept input as a space-separated string and convert it to a list of floats
list_temp = input('Enter a list of temperatures (space-separated): ')

# Convert the input string to a list of floats
list_temp = [float(x) for x in list_temp.split()]

measures(list_temp)
