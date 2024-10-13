def replacer(filename):
    
    with open(filename, 'r') as file:
            # Read the content of the file
            content = file.read()
        
    # replacing
    corrected_content = content.replace('J', 'I')
        
    # Display the corrected content
    print(corrected_content)
    

# Example usage
replacer('words.txt')