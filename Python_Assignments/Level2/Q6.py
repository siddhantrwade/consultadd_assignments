"""
power of 2 checker function

"""

def powerchecker(n):
    
    if n == 1:
        return True
    
    elif n < 1:
        return False
    # Recursive case: divide n by 2 and check again
    else:
        return powerchecker(n / 2)

number = int(input('Enter a number'))

# Check if the number is a power of two and print the result
if powerchecker(number):
    print("is a power of two.")
else:
    print("is not a power of two")