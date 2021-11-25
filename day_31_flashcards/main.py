import csv
import random

from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
CARDBACK = "images/card_back.png"
CARDFRONT = "images/card_front.png"
RIGHT = "images/right.png"
WRONG = "images/wrong.png"

FONT_NAME = "Arial"

# functions for the cards #
WORDS = []
current_word = []
study_list = []

try:
    with open("data/words_to_learn.csv", "r") as word_file:
        reader = csv.reader(word_file)
        for row in reader:
            WORDS.append(row)
        chosen_word = random.choice(WORDS)
        current_word.append(chosen_word)

except FileNotFoundError:
    with open("data/french_words.csv", 'r') as word_file:
        reader = csv.reader(word_file)
        next(reader)
        for row in reader:
            WORDS.append(row)
        chosen_word = random.choice(WORDS)
        current_word.append(chosen_word)




def correct():
    canvas.itemconfig(language_text, text="French")
    print(current_word)
    WORDS.remove(current_word[0])
    next_word()
    canvas.itemconfig(word_text, text= current_word[0][0])
    print(f" length of the words list: {len(WORDS)}")
    if len(WORDS) >0:
        window.after(3000, func=flippy)




def incorrect():

    with open("data/words_to_learn.csv", "a") as word_data:
        writer = csv.writer(word_data)
        writer.writerow(*current_word)

    WORDS.remove(current_word[0])
    canvas.itemconfig(language_text, text="French")
    next_word()
    try:
        canvas.itemconfig(word_text, text= current_word[0][0])
        if len(WORDS) >0:
            window.after(3000, func=flippy)

    except IndexError:
        print("those were the last of the words that you didn't know!")
        print("CONGRATS")


#-----------------------------------------------------------------------#

def next_word():
    chosen_word = random.choice(WORDS)
    current_word.pop()
    current_word.append(chosen_word)




# after the 3 secs transition to the back png and change text to english


def flippy():
    canvas.itemconfig(language_text, text="English")
    canvas.itemconfig(word_text, text= current_word[0][1])
    canvas.itemconfig(card_background, image= back_image)
    print("answer now")

#setting up the UI#

window = Tk()
window.title("Language Flashcards")
window.config(padx= 50, pady= 50, bg= BACKGROUND_COLOR)

window.after(3000, func= flippy)

canvas = Canvas(width= 800, height= 526, highlightthickness= 0)


back_image = PhotoImage(file= CARDBACK)
front_image = PhotoImage(file= CARDFRONT)
right_image = PhotoImage(file= RIGHT)
wrong_image = PhotoImage(file= WRONG)

card_background = canvas.create_image(400, 300, image= front_image)
# have a language text over the card
language_text = canvas.create_text(400, 150, text= "French",font= (FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400, 263, text= current_word[0][0],font= (FONT_NAME, 60, "bold"))
canvas.grid(column= 0, row= 0, columnspan= 2)

# have the word in the foreign language under language text

# want the card to be clickable so that we can turn it over

# other side displays the same info

# two button at the bottom x and a check(user must click card before they can select one
right_button = Button(image= right_image, command= correct)
right_button.grid(column= 1, row= 1)

wrong_button = Button(image= wrong_image, command= incorrect)
wrong_button.grid(column= 0, row= 1)








window.mainloop()




