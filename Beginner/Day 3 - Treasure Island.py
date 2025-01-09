print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
x=input('''You are at a crossroad.
Where do you want to go?
Left or Right?''')
if x=="Right":
          y=input('''Good!
Right is always the right way:)
Now, You have two choices: Forbidden Forest or Green Land?''')
          if y=="Green Land":
                    z=input('''A good choice!
Green Land filled with green flags:)
Now, You have to go through any one of three coloured doors: Red, Blue and Purple?''')
                    if z=="Red":
                              print('''Since you followed a red flag, you have been burned by fire
Game Over!''')
                    elif z=="Blue":
                              print('''Congratulations!
You can find the treasure here!!''')
                    else:
                              print('''The treasure is not here
But you have chosen a world of purple filled with armies and BTS!
So congratulations on finding the real tresure!!''')
          else:
                    print('''There was a monster in the forbidden forest,
It's forbidden for a reason 
Game Over!''')
                    
else:
          print('''There was a lion in the left,
Right is always the right way:)
Game Over!''')
