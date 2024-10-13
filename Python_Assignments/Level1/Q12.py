number = int(input("enter a number "))

reverse_default = 0

while number > 0:

    digit = number%10
    reverse_default = reverse_default * 10 + digit
    number //= 10 

print('Reversed Number', reverse_default)