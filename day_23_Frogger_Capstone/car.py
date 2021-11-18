from turtle import Turtle
import random


class CarTool:
    def __init__(self):
        self.car_list = []

    def car_creator(self, num):
        rand_num = random.randint(1,num)
        if rand_num == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.setx(360)
            new_car.shape("square")
            new_car.shapesize(1, 2, 2)

            colorlist = ["green", "yellow", "red", "purple", "blue", "orange"]
            rand_color = random.choice(colorlist)

            new_car.color(rand_color)

            ynum = random.randint(-250, 250)
            new_car.sety(ynum)
            self.car_list.append(new_car)

    def move(self):
        for car in self.car_list:
            car.backward(10)