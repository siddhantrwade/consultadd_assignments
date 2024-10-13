def count_frequency(elements):
    frequency = {}  # Dictionary to hold the frequency of each element


# Main function to input a list
def main():
    # Input a list from the user
    user_input = input("Enter elements of the list separated by spaces: ")
    # Split the input string into a list of elements
    elements = user_input.split()
    
    # Count the frequency of each element
    frequency_count = count_frequency(elements)
    
    # Print the frequency of each element
    print("Frequency of each element:")
    for element, count in frequency_count.items():
        print(f"{element}: {count}")

# Run the main function
if __name__ == "__main__":
    main()
