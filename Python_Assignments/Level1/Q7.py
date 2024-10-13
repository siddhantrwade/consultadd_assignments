print('Anagram checker, case and space sensitive \n\n')
str1 = input('Enter string 1')
str2 = input('Enter string 2')

if sorted(str1) == sorted(str2):

    print('Strings are anagram')
else: 
    print("Strings are not anagrams")
