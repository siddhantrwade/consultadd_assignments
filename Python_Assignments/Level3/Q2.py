with open("demo.txt", "r") as readfile: 
    a = readfile.readlines()
    print('Data in the file is as follows : -\n')
    print(a)

print('Number of lines in file:',len(a))