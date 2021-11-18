import pandas as pd
import turtle


def get_mouse_click_coor(x,y):
    return x, y

screen = turtle.Screen()
screen.title("State Quiz")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

screen.tracer(0)

states_data = pd.read_csv("50_states.csv")
states_list = states_data.to_dict()


some_list = states_list.values()

states, x, y = some_list


states = list(states.values())
x = list(x.values())
y = list(y.values())


all_state = list(zip(states, x, y))

turtles = []

guessed_states = []

for row in states_data.itertuples(False):
   loc = turtle.Turtle()
   loc.__setattr__("name", row[0])
   state_name = loc.__getattribute__("name")
   loc.goto(row[1], row[2])
   loc.hideturtle()
   turtles.append(loc)




# state_iter = states_data.itertuples(False)
while len(guessed_states) < 50:
    answer = screen.textinput(f"{len(guessed_states)}/50", "Enter the name of a state").title()  # initialization
    for state in turtles:
        if answer == "Exit":
            missing_states = []
            for state in turtles:
                if state not in guessed_states:
                    missing_states.append(state.__getattribute__("name"))
            print(f"states missed: {missing_states}")
            break

        if answer == state.__getattribute__("name"):
            state.write(arg=answer, align="center")
            guessed_states.append(state)







# ghetto way of doing it


#
# cap = answer.title()
# if cap in states:
#     cap = turtle.Turtle()
#     cap.goto(all_state[])
# cap = answer.title()
#
#
# if cap in states:
#     print(cap)
# else:
#     print(states)


#can't do this since it isn't sorted
# st_list = list(set(states_data["state"]))
#
# print(st_list)
#
# print(list(set(states_data["x"])))
#
# print(list(set(states_data["y"])))



# screen.textinput(f"{numcorrect}] /50 states correct", "What's another state's name?")

# answer = screen.textinput("What's a state's name?")
#
# numcorrect = 0
# for i in range(50):

#     answer = screen.textinput(f"{numcorrect}] /50 states correct", "What's another state's name?")


# states_data[states_data.state == "Alabama"]
turtle.mainloop()



