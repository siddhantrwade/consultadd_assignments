def string_checker(text, character):
    # check if text starts with character
    check_start = lambda s, c: s.startswith(c)
    return check_start(text, character)

# Example usage
input_string = input("Enter a string: ")
character = input("Enter a character: ")

if string_checker(input_string, character):
    print('True')
else:
    print('False')