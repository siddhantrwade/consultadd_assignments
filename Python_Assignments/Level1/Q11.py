number = int(input("Enter a number"))

while number >= 10:  # Continue until the number is a single-digit
    sum_value = sum(int(digit) for digit in str(number))  # Sum the digits
    

print('Current sum is ', sum_value)