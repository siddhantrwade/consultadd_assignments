def count_vowels(text):
    
    vowels = 'aeiouAEIOU'
    count = 0

    for item in text:
        if item in vowels:
            count += 1 

    return count

# Example usage
sample_input = input('Enter string')
vowel_count = count_vowels(sample_input)
print(f"The number of vowels in '{sample_input}' is: {vowel_count}")