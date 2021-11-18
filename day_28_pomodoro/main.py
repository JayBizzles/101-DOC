from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25*60
SHORT_BREAK_MIN = 5*60
LONG_BREAK_MIN = 20*60
reps = 0
check_text = '✓'

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

def iseven(num):
    if num % 2 == 0:
        return True
    else:
        return False

def start_timer():
    global reps
    reps += 1


    # #if it's the 1/3/5/7 rep then:
    # countdown(WORK_MIN)
    # #if it's the 8th rep then:
    # countdown(LONG_BREAK_MIN)
    # #if it's the 2/4/6 rep then:
    # countdown(SHORT_BREAK_MIN)
    if reps == 8:
        countdown(LONG_BREAK_MIN)
    elif iseven(reps):
        countdown(SHORT_BREAK_MIN)
    else:
        countdown(WORK_MIN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):

    global reps
    # WORK_MIN divided by 60 will give the mins
    count_mins = math.floor(count / 60)

    # remainder of the same numbers with provide the secs
    count_secs = count % 60

    #example of using dynamic typing
    if count_secs < 10:
        count_secs = f"0{count_secs}"

    canvas.itemconfig(timer_text, text= f"{count_mins}:{count_secs}")
    if count > 0:
        window.after(1000, countdown, count-1)
    else:
        start_timer()
        #add a check mark to the bottom eachtime

        #have to make a copy of the old frame see stackoverflow

        check = Label(bottom_frame, text=check_text, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 10, "bold"))
        check.grid(column= 1+ reps, row= 3)




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx= 100, pady= 50, bg= YELLOW)



canvas = Canvas(width= 220, height= 224, bg= YELLOW, highlightthickness= 0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(110, 112, image= tomato_img)
timer_text = canvas.create_text(110,130,text= f"{WORK_MIN}", fill= "white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column= 1,row= 2)


start_button = Button(text= "start", command= start_timer)
start_button.grid(column= 0,row= 3)

timer_ = Label(text= "Timer", fg = GREEN, font = (FONT_NAME, 50, "italic"), bg= YELLOW)
timer_.grid(column= 1,row= 0)

check = Label(text= check_text, fg = GREEN, bg= YELLOW, font = (FONT_NAME, 10, "bold"))
check.grid(column= 1,row= 3, columnspan= 3)

reset_button = Button(text= "reset")
reset_button.grid(column= 3,row= 3)

bottom_frame = tkinter.Frame(window)
bottom_frame.grid(row=3, columnspan=3)

window.mainloop()
