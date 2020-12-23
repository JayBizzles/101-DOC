#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = []
string = ""
string2 = ""
for i in range(nr_letters):
    password.append(random.choice(letters))

for i in range(nr_symbols):
    password.append(random.choice(symbols))

for i in range(nr_symbols):
    password.append(random.choice(numbers))

# for i in range(len(password)):
#     string[i] = password[i]

# print(string)

#the above code doesn't work because strings are immutable in python

for i in password:
    string += i

print(string)

# This code is the correct code

#to randomize the code so that the datatypes are not in a particular order
random.shuffle(password)

for i in password:
    string2 +=i 

print(string2)