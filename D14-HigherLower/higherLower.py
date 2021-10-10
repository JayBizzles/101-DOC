from game_data import data
import art
import random

print(art.logo)

COUNTER = 0
DED = False

def higherLower():
        celeb1, celeb2 = random.choices(data, k=2)
        eval(celeb1,celeb2)

def eval(celeb1, celeb2):
    global COUNTER
    global DED
    name1, cnt1, occupation1, origin1 = celeb1.values()
    name2, cnt2, occupation2, origin2 = celeb2.values()

    print(f"{name1} is a {occupation1} from {origin1}")
    print(art.vs)
    print(f"{name2} is a {occupation2} from {origin2}")

    usrval = int(input("> input the account you think has the higher follower count: "))
    while DED is False:
        if cnt1 > cnt2 and usrval == 1:
            print("here 1")
            COUNTER+=1
            celeb2.clear()
            celeb2 = random.choice(data)
            eval(celeb1, celeb2)
        elif cnt1 < cnt2 and usrval == 2:
            print("here 2")
            COUNTER+=1
            celeb1.clear()
            celeb1 = random.choice(data)
            eval(celeb1, celeb2)
        else:
            print(f"Incorrect \t \t HighScore: {COUNTER}")
            DED = True
            break
higherLower()