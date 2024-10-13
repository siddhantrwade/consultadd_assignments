students = ['Sam', 'Alice', 'Mona']
subjects = ['Commerce', 'Science', 'Computer']

dict_sample = {}
for i in range(len(students)):
    dict_sample[students[i]] = subjects[i]

print("Dictionary using for loop:")
print(dict_sample)

dict_sample1 = {students[i]: subjects[i] for i in range(len(students))}

print("\nDictionary using dictionary comprehension:")
print(dict_sample1)
