import tkinter

def button_clicked():
    print("I was just clicked")
    something = input.get()
    my_label.config(text=something)

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)


# Label Creation
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack() # places and centers label on screen

# these 2 accomplish the same thing
my_label["text"] = "new text"
my_label.config(text="new text")
my_label.grid(column=0, row=0)
my_label.config(padx= 20, pady=20)
# Button

button = tkinter.Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

newbutton = tkinter.Button(text="new button")
newbutton.grid(column= 2, row= 0)

# Entry

input = tkinter.Entry(width=10)
input.grid(column= 3, row= 2)









window.mainloop()

#playground.py

# # can set unlimited positional arguments
# def add(*args):
#     sum = 0
#     for num in args:
#         sum+=num
#     return sum
#
# print(add(3,5,9,10,2))
#
# # can set unlimited keyword arguments
# def calculate(n,**kwargs):
#     for key, value in kwargs.items(): # return
#         print(key, value)
# calculate(2,add=3, multiply=4)
#
# class Car:
#     def __init__(self, **kwargs):
#         self.make = kwargs.get("make")
#         self.model = kwargs.get("model")
#
# my_car = Car(make = "Nissan")
# print(my_car.make)