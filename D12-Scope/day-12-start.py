############################ Scope ##############################

enemies = 1 #global variable

def increase_enemies(): #local variable
    global enemies #use gloabl keyword to access global scope inside of a function
    enemies +=3
    print(f"enemies inside function: {enemies}")
increase_enemies()
print(f"enemies outside function: {enemies}")

player_health = 10

def game():
    def drink_potion():
        potion_strength = 2
        print(player_health) # can call player health inside because it is global
    drink_potion() #have to call drink_potion inside of game because it is nested
#def drink_potion() this will not work
print(player_health)

#global constants

PI = 3.14159


