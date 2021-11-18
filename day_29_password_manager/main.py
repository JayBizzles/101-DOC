from tkinter import *
from tkinter import messagebox
import random
import pyperclip
FONT_NAME = "Arial"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def pass_generation():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)

    letter_list = [random.choice(letters) for i in range(nr_letters)]
    symbol_list = [random.choice(symbols) for i in range(nr_symbols)]
    number_list = [random.choice(numbers) for i in range(nr_numbers)]

    password_list = letter_list + symbol_list + number_list

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    password_entry.insert(index= 0, string= password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_inputs():
    file_path = "data.txt"

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title= "Error", message= "you are missing one of the required fields")
    else:
        is_ok = messagebox.askokcancel(title= website, message= f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")

    if is_ok:
        pyperclip.copy(password)
        with open(file_path, "a") as data:
            input_list = [website, email, password]

            strings = " |".join(input_list)
            data.write(strings + "\n")

            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")

canvas = Canvas(width= 220, height= 220, highlightthickness= 0)
lock_img = PhotoImage(file= "logo.png")
canvas.create_image(110, 112, image= lock_img)
canvas.grid(column= 1, row= 2)

website_text = Label(text= "Website: ",font=(FONT_NAME, 10, "bold"))
website_text.grid(column= 0, row= 3)

website_entry = Entry(width= 35)
website_entry.focus()

website_entry.grid(column= 1, row=3, columnspan= 2)

email_text = Label(text= "Email: ",font=(FONT_NAME, 10, "bold"))
email_text.grid(column= 0, row= 4)

email_entry= Entry(width= 35)
email_entry.insert(0,"example@mail.com")

email_entry.grid(column= 1, row=4, columnspan= 2)

password_text = Label(text= "Password: ",font=(FONT_NAME, 10, "bold"))
password_text.grid(column= 0, row= 5)


password_entry= Entry(width= 21)

password_entry.grid(column= 1, row=5, columnspan= 2)

generate_button = Button(text= "Generate Password", font=(FONT_NAME, 10, "bold"), command= pass_generation)
generate_button.grid(column= 3, row= 5)

add_button = Button(text= "Add", font=(FONT_NAME, 10, "bold"), width= 36, command= save_inputs)
add_button.grid(column= 1, row= 6, columnspan= 2)

window.mainloop()