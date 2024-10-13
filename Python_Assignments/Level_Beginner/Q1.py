number = input('Input the number you wish to test ')
number = int(number)

if (number % 3 == 0) and (number % 5 == 0):

    print('Consultadd - Python Training')
elif number % 3 == 0:
        print("Consultadd")
elif number % 5 == 0:
        print("Python Training")
else: print('Selected Number is not divisible')