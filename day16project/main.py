
# from turtle import Turtle, Screen
#
# timmy = Turtle()
#
# print(timmy)
# timmy.shape("turtle")
# timmy.color("chocolate4")
# timmy.tilt(45)
# my_screen = Screen()
# my_screen.exitonclick()
# print(my_screen.canvheight)

import prettytable

x = prettytable.PrettyTable()

# x.field_names = ["PokemonName", "Type"]
x.add_column("PokemonName", ["Pikachu","Squirtle", "Charmander"])
x.add_column("Type", ["Electric","Water", "Fire"])

x.align = "r"

print(x)