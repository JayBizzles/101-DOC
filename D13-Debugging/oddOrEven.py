# spot the problems with the code and modify it to fix its problems

number = int(input("Which number do you want to check?"))

if number %2 == 0: # bug: =
    print("This is an even number")
else:
    print("This is an odd number")