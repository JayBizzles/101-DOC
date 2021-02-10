# How to initialize a python ditionary
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A oiece of code that you can easily call over and over again",
}

#Accessing the value of a dictionary by using the key associated with it
print(programming_dictionary["Bug"])

#Adding new items to the dictionary by creating a key and assigning a value to it
programming_dictionary["Loop"] = "The action of doing something over and over again."

print(programming_dictionary)

#Creating an empty dictionary
empty_dictionary = {}

#wiping the contents of a dictionary
#programming_dictionary = {}

#editing a new item to a dictionary
programming_dictionary["Bug"] = "A moth in your computer."

print(programming_dictionary["Bug"])

#looping over the keys in a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

#Nesting - Putting a list inside of a dictionary or vice versa

#{
    # key: [list]
    # key2: {dict}
# }

capitals = {
    'France': 'Paris',
    'Germany': 'Berlin',
}

#nesting a dictionary in a dictionary
travel_log = {
    'France': {"cities_visited" : ['Paris', 'Lille', 'Dijon'], "total_visits": 12},
    'Germany': {"cities_visited" : ['Berlin', 'Hanburg', "Stuggart"],  "total_visits": 5},
}

#nesting a dictionary in a list

travel_log = [
    {'country': 'France',
    "cities_visited" : ['Paris', 'Lille', 'Dijon'],
    "total_visits": 12
    },
    {'country': 'Germany',
    "cities_visited" : ['Berlin', 'Hanburg', "Stuggart"],
    "total_visits": 5
    },
]