start = int(input('Provide starting number'))
end = int(input('Provide ending number'))

if start > end: 
    print('Starting number is greater than end, hene swapped')
    start, end = end, start

list_odd_numbers = []

for i in range(start, end + 1):

    if i % 2 != 0: 

        list_odd_numbers.append(i)

sum_value = sum(list_odd_numbers)
print('Sum of odd numbers is: ', sum_value )
