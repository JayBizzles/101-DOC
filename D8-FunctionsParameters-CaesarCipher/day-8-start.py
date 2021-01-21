# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.


def greet():
    print("Help")
    print("Help")
    print("Help")

greet()

# def greet_with_name(name):
#     print(f'Hello {name}')
#     print(f'Hello {name}')
#     print(f'Hello {name}')

# greet_with_name("jamal")

#Functions with more than 1 input
def greet_with_name(name, age):
    return f'Hello {name}, you look like you are about {age} years old!'

print(greet_with_name("Johnny", "7"))

#keyword arguments
def my_function(a,b,c):
    print(f'This is {a}')
    print(f'This is {b}')
    print(f'This is {c}')

my_function(c=1,b=3,a=5)
my_function(1,3,5)

for i in range(2,10):
    print(i)
#Now call greet_with_name() but use keyword arguments instead of positonal arguments

print(greet_with_name(age=25, name="Timmy"))