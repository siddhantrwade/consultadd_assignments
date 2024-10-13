

def exception_handler(list_sample):

    n = len(list_sample)

    try:

        element = list_sample[n+2]
        print(f"Extracting element at index {n+2} as {element}")

    except IndexError:

        print(f"Error: Index {n+2} is out of range")


list_sample = input('enter a list: ')

exception_handler(list_sample)