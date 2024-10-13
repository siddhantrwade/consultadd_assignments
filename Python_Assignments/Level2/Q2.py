def list_uniques(list1): 
    
    uniques = set(list1)

    list_uniques = list(uniques)

    return list_uniques

list_input = input('Enter a list')

print('Uniues in the list are: ', list_uniques(list_input))
print('Uniques in list by set are ', set(list_input))


