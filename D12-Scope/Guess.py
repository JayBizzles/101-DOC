import random

LIVES = 10
NUM = random.randint(1,100)

ans = input("""Welcome to the number guessing game!\n
I'm thinking of a number between 1 and 100\n
Choose a difficulty. Type 'easy' or hard:""")

def easy():
    global LIVES
    prompt = ("Make a guess:")
    guess = int(input(prompt))

    while LIVES != 0:
        if guess < NUM:
            print("You guess too low")
            LIVES-=1
            print(LIVES)
            return hard()
        elif guess> NUM:
            print("You guess to high")
            LIVES-=1
            print(LIVES)
            return hard()
        else:
            print("You guessed the number!")
            print(LIVES)
            return True
    pass

def hard():
    global LIVES
    prompt = ("Make a guess:")
    guess = int(input(prompt))

    while LIVES != 0:
        if guess < NUM:
            print("You guess too low")
            LIVES-=1
            print(LIVES)
            return hard()
        elif guess> NUM:
            print("You guess to high")
            LIVES-=1
            print(LIVES)
            return hard()
        else:
            print("You guessed the number!")
            print(LIVES)
            return True

#CHECK THAT MUTATES THE global LIVES variable
def lifecheck():
    global LIVES
    LIVES -=5
    return LIVES

if ans == 'easy':
    easy()
elif ans == 'hard':
    lifecheck()
    hard()