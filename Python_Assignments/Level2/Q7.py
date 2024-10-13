



list_sample = [7, 2, 5, 1, 9, 3]
print('List is', list_sample)
list_sorted = sorted(list_sample)

n = len(list_sorted)

# if odd numbered list then return number at the center

if n%2 == 1:

    median = list_sorted[n//2]
    print('median: ', `median)

else: 

    centerleft = list_sorted[n // 2-1]
    centerright = list_sorted[n //2]
    median = (centerleft+centerright)/2
    print('median: ', median)


    

