# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇



if (year % 4 == 0):
    if(year % 100 == 0):
        if(year % 400 == 0):
            print("Leap Year.")
        else:
            print("Not a Leap Year.")
    else:
        print("Is a Leap Year.")
else:
    print("Not a Leap Year")

    # we use nested if's in this case because even if year passes one of the loops we still have other conditions that needed to be checked

    # use elif's when we can ignore a condition as soon as we get our answer from another