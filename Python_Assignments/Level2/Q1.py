list1 = input('Enter frist list ')
list2 = input('Enter second list ')


first_set = set(list1)
second_set = set(list2)

if first_set & second_set:

    print('Common elements are: ',first_set & second_set)
else: 
    print('No common elements found')