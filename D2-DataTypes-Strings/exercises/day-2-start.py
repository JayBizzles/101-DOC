False

num_char = len(input("what is your name?"))

#print("your name has "+ num_char + "characters")

#returns error : TypeError: can only concatenate str (not "int") to str

#happens because num_char is now an int and we cannot concatenate strings with ints

print(type(num_char))

#use type() to check what the data type is

# we can convert int to string by using str()

new_num_char = str(num_char)

print("your name has "+ new_num_char + "characters")