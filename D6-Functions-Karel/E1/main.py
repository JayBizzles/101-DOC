#code for the hurdle challenges on reeborg.ca

def jump():
    turn_left()
    move()
    turn_left()
    turn_left()
    move()
    turn_right()
    move()
    turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def up_one():
    move()

while not at_goal():
    if front_is_clear():
        if right_is_clear():
            turn_right()
            move()
        else:
            move()
    elif wall_in_front():
        turn_left()
        up_one()
    
        
        
