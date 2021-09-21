#Functions with outputs

def function(fname,lname):
    fullname = fname.title() + lname.title()
    return fullname

print(function('jamal', 'bills'))

#Functions that have more than one return statement

#the return statement ends the function

def formatName(fname, lname):
    if fname == '' or lname == '':
        return "There were no inputs provided"

    formated_f_name = fname.title()
    formated_l_name = lname.title()

    return f'{formated_f_name} {formated_l_name}'

print(formatName(input("What is your first name? "), input("What is your last name? ")))

def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
    
result = outer_function(5, 10)
print(result)