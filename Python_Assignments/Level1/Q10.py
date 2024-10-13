text = input('Enter a text :')

content = text.split()

reversed_content = content[::-1]

reversed_text = ' '. join(reversed_content)



print('Reverse Content is:\n', reversed_text)