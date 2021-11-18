
import pandas as pd
# # we will be making a program that takes a name and brakes it down to its nato equivalent
#
# # should use a dictionary to map letters with their counterparts
#
# # list comprehension
# numbers = [1,2,3]
# new_numbers = [num+1 for num in numbers]
#
# # this works because the range is an iterable
# new_i = [i*2 for i in range(1,5)]
#
# # conditional list comprehension with if
# names = ["Jim", "Jam", "Sam", "Jamal"]
#
# short_names = [name for name in names if len(name) < 4]
#
# long_names = [name.upper() for name in names if len(name)>3]
#
# # coding challenge 2
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
#
# result = [num for num in numbers if num%2 == 0]
#
#
# # comparing numbers from different list
#
# file1_path ="file1"
# file2_path ="file2"
#
# with open(file1_path, 'r') as f1, open(file2_path, 'r') as f2:
#     line1 = f1.readlines()
#     line2 = f2.readlines()
#     result = [num for num in line1 if num in line1 and line2]
#
# print(result)
#
# # dictionary comprehension
#
# # new_dict = {new_key:new_value for item in list}
#
# # making a dictionary from an existing dicitonary
# # new_dict = {new_key:new_value for (key,value) in dict.items()}
#
# import random
#
# names = ["Jim", "Jam", "Sam", "Jamal"]
#
# student_scores ={name:random.randint(1,100) for name in names}
#
# passed_students = {name:score for (name,score) in student_scores.items() if score > 70}
#
#
# # print(f"student score: {student_scores}")
# # print(f"passed students: {passed_students}")
#
# # coding exercise 1
#
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
#
# sentence_list = sentence.split()
#
# result = {word:len(word) for word in sentence_list}
#
#
#
# # coding exercise 2
#
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
#
# weather_f = {day:(temp * 9/5) + 32 for (day, temp) in weather_c.items()}
#
# # print(weather_f)
#
# #looping through pandas dataframe
#
# import pandas as pd
#
# name_data_frame = pd.DataFrame(names)
#
#
# # loop through rows of a dataframe
#
# for (index, row) in name_data_frame.iterrows():
#     print(row)

nato_data = pd.read_csv("nato_phonetic_alphabet.csv")

# this is how this works!!!!!
new_dict = {row.letter:row.code for (index, row) in nato_data.iterrows()}


usrinput = input("type some stuff").upper()

input_list = list(usrinput)

code_words = [value for (key,value) in new_dict.items() if input_list.__contains__(key)]

print(code_words)