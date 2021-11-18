from turtle import Turtle



# blocks = []
#
# for position in positions:
#     new_segment = Turtle("square")
#     new_segment.penup()
#     new_segment.color("white")
#     new_segment.goto(position)
#     blocks.append(new_segment)
#
#
#
# running = True
#
# while running:
#     screen.update()
#     time.sleep(0.5)
#     for block in blocks:
#         block.forward(20)





# we have to make the blocks move like a snake:

    # move front block and the rest goto current pos of the one ahead


    # control the snake using wasd

    # make food that shows up on screen: when food collected make new food and add new turtle object to the last position

    # make a scoreboard for the game

    # detect collision with the wall

    # detect collision with itself




#           still accessible from the outside
# class car:
#
#     def __init__(self, name, mileage):
#         self._name = name                #protected variable
#         self.mileage = mileage
#
#     def description(self):
#         return f"The {self._name} car gives the mileage of {self.mileage}km/l"
#
#
# obj = car("BMW 7-series", 39.53)
#
# # accessing protected variable via class method
# print(obj.description())
#
# # accessing protected variable directly from outside
# print(obj._name)
# print(obj.mileage)

#           not accessible from the outside using __

# class Car:
#     def __init__(self, name, mileage):
#         self.__name = name              #private variable
#         self.mileage = mileage
#
#     def description(self):
#         return f"The {self.__name} car gives the mileage of {self.mileage}km/l"
#
#
# obj = Car("Bmw 7-series", 39.53)
# print(obj.description())
#
# print(obj.mileage)
#
# # cant access the variable because it it private:
# # print(obj.__name)
#
# # but we can access the variable if we print the mangled name
# print(obj._Car__name)

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
class Snake:

    # make a snake

    def __init__(self):
        self.snakelist = []
        self.start()
        self.head = self.snakelist[0]
        self.game_state = True


    # need to give each snake a position

    # could be useful later
    def start(self):
        for i in range(3):
            obj = Turtle(shape="square")
            obj.penup()
            obj.color("white")
            obj.goto(POSITIONS[i])
            self.snakelist.append(obj)



    # have the first snake moveforward
    # all snake got the old position of the one in front of it
    # and then we update the screen and turn screen.tracer off
    def move(self):
        for seg_num in range(len(self.snakelist) -1,0,-1):
            new_x = self.snakelist[seg_num-1].xcor()
            new_y = self.snakelist[seg_num - 1].ycor()
            self.snakelist[seg_num].goto(new_x,new_y)
        self.head.forward(20)
        print(self.head.position())

    def move_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def move_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def move_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def move_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def add_to_tail(self):
        obj = Turtle(shape="square")
        # obj.hideturtle()
        obj.penup()
        obj.color("white")
        self.snakelist.append(obj)

    def reset(self):
        for seg in self.snakelist:
            seg.goto(1000,1000)
        self.snakelist.clear()
        self.start()
        self.head = self.snakelist[0]