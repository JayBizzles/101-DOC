# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()

name = name1 + name2

score1 = name.count("t") + name.count("r") + name.count("u") + name.count("e")
score2 = name.count("l") + name.count("o") + name.count("v") + name.count("e")

score = str(score1) + str(score2)

if int(score) < 10 or int(score) > 90:
    print(f"Your score is {score}, yo go together like coke and mentos.")
elif int(score) >= 40 and int(score) <= 50:
    print(f"Your score is {score}, you are alright together.")

else:
    print(f"Your score is {score}.")