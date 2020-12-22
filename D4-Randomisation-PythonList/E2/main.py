import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#We can use random.choice when we want to randomly pick an item from a list
loser = random.choice(names)

#Or solving is the way that the README said to
loser = names[random.randint(0,len(names))]

print(f"{loser} is going to buy the meal today!")
