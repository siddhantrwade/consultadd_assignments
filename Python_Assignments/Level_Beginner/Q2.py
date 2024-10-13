user_string = str(input('Enter a string '))

letters_count = 0
digits_count = 0
    
for char in user_string:
    if char.isalpha():  # Check if the character is an alphabet
            letters_count += 1
    elif char.isdigit():  # Check if the character is a digit
            digits_count += 1
    
# Print the results
print(f"Alphabets: {letters_count} & Numbers: {digits_count}")
