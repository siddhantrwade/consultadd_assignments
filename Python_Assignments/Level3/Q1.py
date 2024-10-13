'''
with open("test.txt","w") as testtxt:
    testtxt.write("Hello I am a file")
'''

with open("test.txt", "r") as readfile: 
    a = readfile.readlines()
    print('Data in the file is as follows : -\n')
    print(a)

text = str(a[0])
text_split = text.split()

if (len(text) % 2) == 0:
    print(text[0:len(text)])
else:
    print(text[0:len(text)+1])
