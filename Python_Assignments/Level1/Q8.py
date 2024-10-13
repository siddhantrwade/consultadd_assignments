num1 = int(input("Enter 1st number"))
num2 = int(input("Enter 2nd number"))

while num2:

    num1, num2 = num2, num1 % num2

print(abs(num1 * num2) // num1)