from tkinter import *
KM_CONVERSION = 1.609344

def conversion():
    num_miles = int(input.get())
    result = num_miles * KM_CONVERSION
    number_label.config(text=str(result))


window = Tk()
window.title("My First GUI Program")
window.minsize(width=300, height=300)
window.config(padx=20, pady=20)

input = Entry(width= 10)
input.grid(column=2, row=0)

equal_text = Label(text="is equal to", font=("Arial", 15, "bold"))
equal_text.grid(column=1, row= 1)

miles_label = Label(text= "Miles", font=("Arial", 15, "bold"))
miles_label.grid(column=3,row=0)

number_label = Label(text = "0", font=("Arial", 10, "bold"))
number_label.grid(column=2, row=1)

km_label = Label(text= "Km", font=("Arial", 15, "bold"))
km_label.grid(column =3, row=1 )

calc_button = Button(text="Calculate", command=conversion)
calc_button.grid(column=2, row=2)



window.mainloop()

