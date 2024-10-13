number = int(input('Enter a number'))

sum_of_divisors = 0

   
for i in range(1, number):  
    if number % i == 0:  # Check if i is a divisor of n
        sum_of_divisors += i  # Add to the sum if it is a divisor

flag_sum = sum_of_divisors == number

if flag_sum == True:
    print('Number meets requirements for perfect number')
else: print('Number is not a perfect number')
