import random

#prints random integer from 1 - 4 (inclusive)
random_int = random.randint(1,4)
print(random_int)

#prints random float from 0 - 0.999999 (inclusive)
random_float = random.random()

print(random_float)

print(random_int + random_float)

love_score = random.randint(1,100)
print(f"Your love score is {love_score}")

#Lists

fruits = ['item1', 'item2']

#list called fruits that holds 2 string elements

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "apples", "oranges"]
vegetables = ["Spinach", "Lettuce"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1])