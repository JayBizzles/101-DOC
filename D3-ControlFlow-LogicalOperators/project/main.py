print('''
***********************************************************************************************************************************************************************
  _,-----,____g===;,
<'.._____,-------g  ;
                   \   \,
                     q   q,
                      q    q,
                     [='     q
                       `;  O  p
                         k  O  p -{0
                          l  O  p -o
                          ,i     p
                           P  O   |
                         q:|   O| |BD
                            [   | P b
                            |   |  |____________
                          [ |   |  |\         /
                          | '   |  P :       ;
                          | [   0   Q:  ( )  ;
                           [ P  ( )  |;  ( ) ;
                           :Q  ( )  V        p
                            \   [           ;
                             \',     O    /
                               ' ; _ . '
********************************************************************************************************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice1 = input("You're at a crossroad, where do you want to go? Type 'left' or 'right\n").lower()

if choice1 == "left":
    #continue in the game
    choice2 = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n").lower()
        if choice3 == "red":
            print("Room is on fire. Game Over")
        elif choice3 == "yellow":
            print("Congrats. You found the treasure and won the game")
        elif choice3 == "blue":
            print("Shark door. Game Over.")
    else:
        print("You die to a shark. Game Over.")
else:
    print("You fell into a hole. Game Over.")


